#!/usr/bin/env python
# -*- coding:utf-8 -*-
import functools
import inspect
import os

from initpy.templates import blank, falcon, flask, tornado_web
from initpy.exceptions import RootPathDoesNotExists


def name_validator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(func, *args, **kwargs)

        if func_args.get('validate'):
            _filter = "!@#$%^&*()-+=[]{}|\"'."
            name = func_args.get('name').replace('.py', '')\
                                        .replace('.html', '')\
                                        .replace('.txt', '')

            if (len(list(set(list(name)).intersection(list(_filter)))) > 0
                    or name[0].isdigit()):
                title = func.__name__.split('_')[1].title()
                raise globals()['Invalid' + title + 'Name']

        return func(*args, **kwargs)
    return wrapper


class Creator(object):

    errors = []
    root_path = None

    def __init__(self, root_path):
        if not os.path.isdir(root_path):
            raise RootPathDoesNotExists
        self.root_path = root_path

    @name_validator
    def create_file(self, _path, name, template, validate=True):
        file_path = os.path.join(_path, name)
        with open(file_path, 'w') as _file:
            _file.write(template)

    @name_validator
    def create_folder(self, _path, name, validate=True):
        try:
            folder_path = os.path.join(_path, name)
            os.mkdir(folder_path)
        except OSError:
            self.errors.append('Creating skipped: '+name+' already exists')

    def create_module(self, _path, name, template=blank.python):
        self.create_folder(_path, name)

        module_path = os.path.join(_path, name)
        self.create_file(module_path, '__init__.py', template, False)


class FlaskCreator(Creator):

    def create_app(self, _path, module):
        self.create_module(_path, "app", 
                           flask.app_init.substitute(module=module))
        app_path = os.path.join(_path, "app")

        self.create_folder(app_path, "static")
        self.create_templates(app_path, module)
        self.create_app_module(app_path, module)

    def create_app_module(self, _path, name):
        self.create_folder(_path, name)
        module_path = os.path.join(_path, name)

        self.create_file(module_path, "__init__.py", 
                         flask.module_init.substitute(module=name), False)
        self.create_file(module_path, "views.py", 
                         flask.module_views.substitute(module=name))
        self.create_file(module_path, "models.py", blank.python)

    def create_templates(self, _path, module):
        self.create_folder(_path, "templates")
        template_path = os.path.join(_path, "templates")

        self.create_file(template_path, "base.html", flask.base_html)
        self.create_folder(template_path, module)
        self.create_file(os.path.join(template_path, module), "index.html",
                         flask.module_html)

    def create_requirements(self, _path):
        self.create_folder(_path, "requirements")
        self.create_file(os.path.join(_path, "requirements"), "dev.txt",
                         flask.requirements)

    def create_project(self, name, module):
        self.create_folder(self.root_path, name)
        project_path = os.path.join(self.root_path, name)

        self.create_file(project_path, "manage.py", flask.manager)
        self.create_app(project_path, module)
        self.create_requirements(project_path)


class TornadoCreator(Creator):

    def create_handlers(self, _path, name):
        self.create_module(_path, "handlers")
        handlers_path = os.path.join(_path, "handlers")
        self.create_file(handlers_path, name+".py", tornado_web.tornado_handler)

    def create_requirements(self, _path):
        self.create_folder(_path, "requirements")
        self.create_file(os.path.join(_path, "requirements"), "dev.txt",
                         tornado_web.requirements)

    def create_project(self, name, module):
        self.create_folder(self.root_path, name)
        project_path = os.path.join(self.root_path, name)
        
        self.create_file(project_path, "app.py", tornado_web.tornado_app)
        self.create_file(project_path, "urls.py",
                         tornado_web.tornado_urls.substitute(module=module))

        self.create_handlers(project_path, module)
        self.create_requirements(project_path)


class FalconCreator(Creator):

    def create_app(self, _path, module):
        args = dict(module=module, module_title=module.title())

        self.create_module(_path, "app",
                           falcon.app_init.safe_substitute(args))
        app_path = os.path.join(_path, "app")

        self.create_middleware(app_path)
        self.create_models(app_path, module)
        self.create_app_module(app_path, module)

    def create_app_module(self, _path, name):
        args = dict(module=name, module_title=name.title())

        self.create_folder(_path, 'resources')
        module_path = os.path.join(_path, 'resources')

        self.create_file(module_path, "__init__.py",
                         falcon.resource_init.safe_substitute(args), False)
        self.create_file(module_path, "{}.py".format(name),
                         falcon.resource_controller.safe_substitute(args))

    def create_models(self, _path, name):
        self.create_module(_path, "models")
        models_path = os.path.join(_path, "models")
        self.create_file(models_path, "__init__.py", blank.python)
        self.create_file(models_path, "{}.py".format(name), blank.python)

    def create_middleware(self, _path):
        self.create_module(_path, "middleware")
        middleware_path = os.path.join(_path, "middleware")
        self.create_file(middleware_path, "__init__.py", blank.python)

    def create_requirements(self, _path):
        self.create_folder(_path, "requirements")
        self.create_file(os.path.join(_path, "requirements"), "dev.txt",
                         falcon.requirements)

    def create_project(self, name, module):
        self.create_folder(self.root_path, name)
        project_path = os.path.join(self.root_path, name)

        self.create_file(project_path, "manage.py", falcon.manager)
        self.create_app(project_path, module)
        self.create_requirements(project_path)


def downloader(args):
    url = args.download
    from urllib2 import urlopen, HTTPError
    try:
        res = urlopen(url)
    except HTTPError:
        from initpy.prompt import color_print
        color_print("Wrong downloadable url!", "red")
        return
    from initpy.compact import StringIO
    from zipfile import ZipFile, BadZipfile
    try:
        template_zip = ZipFile(StringIO(res.read()))
    except BadZipfile:
        from initpy.prompt import color_print
        color_print("initpy only support zip file!", "red")
        return
    from os import path, getcwd, mkdir
    proj_path = path.join(getcwd(), args.name)
    try:
        mkdir(proj_path)
    except OSError:
        # Folder Exists
        pass
    zip_root = template_zip.namelist()[0]
    for fn in template_zip.namelist()[1:]:
        file_name = fn.replace(zip_root, '')
        file_path = path.join(proj_path, file_name)
        if file_path.endswith('/'):
            try:
                mkdir(file_path)
            except OSError:
                # Folder Exists
                pass
        else:
            _file = open(file_path, 'w')
            _file.write(template_zip.read(fn))
            _file.close()

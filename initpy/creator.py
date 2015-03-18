#!/usr/bin/python
# -*- coding:utf-8 -*-
import functools
import inspect
import os

from initpy import templates
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

    def create_module(self, _path, name, template=templates.blank):
        self.create_folder(_path, name)

        module_path = os.path.join(_path, name)
        self.create_file(module_path, '__init__.py', template, False)


class FlaskCreator(Creator):

    def create_app(self, _path, module):
        self.create_module(_path, "app", 
                            templates.app_init.substitute(module=module))
        app_path = os.path.join(_path, "app")

        self.create_folder(app_path, "static")
        self.create_templates(app_path, module)
        self.create_app_module(app_path, module)

    def create_app_module(self, _path, name):
        self.create_folder(_path, name)
        module_path = os.path.join(_path, name)

        self.create_file(module_path, "__init__.py", 
                        templates.module_init.substitute(module=name), False)
        self.create_file(module_path, "views.py", 
                        templates.module_views.substitute(module=name))
        self.create_file(module_path, "models.py", templates.blank)

    def create_templates(self, _path, module):
        self.create_folder(_path, "templates")
        template_path = os.path.join(_path, "templates")

        self.create_file(template_path, "base.html", templates.base_html)
        self.create_folder(template_path, module)
        self.create_file(os.path.join(template_path, module), "index.html",
                        templates.module_html)

    def create_requirements(self, _path):
        self.create_folder(_path, "requirements")
        self.create_file(os.path.join(_path, "requirements"), "dev.txt", 
                        templates.flask_requirements)

    def create_project(self, name, module):
        self.create_folder(self.root_path, name)
        project_path = os.path.join(self.root_path, name)

        self.create_file(project_path, "manage.py", templates.manager)
        self.create_app(project_path, module)
        self.create_requirements(project_path)


class TornadoCreator(Creator):

    def create_handlers(self, _path, name):
        self.create_module(_path, "handlers")
        handlers_path = os.path.join(_path, "handlers")
        self.create_file(handlers_path, name+".py", templates.tornado_handler)

    def create_requirements(self, _path):
        self.create_folder(_path, "requirements")
        self.create_file(os.path.join(_path, "requirements"), "dev.txt", 
                        templates.tornado_requirements)

    def create_project(self, name, module):
        self.create_folder(self.root_path, name)
        project_path = os.path.join(self.root_path, name)
        
        self.create_file(project_path, "app.py", templates.tornado_app)
        self.create_file(project_path, "urls.py", 
                        templates.tornado_urls.substitute(module=module))

        self.create_handlers(project_path, module)
        self.create_requirements(project_path)

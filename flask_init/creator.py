#!/usr/bin/python
# -*- coding:utf-8 -*-
import functools
import inspect
import os

from .exceptions import (InvalidFileName, InvalidFolderName,
                         RootPathDoesNotExists)
from .templates import blank_template


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

    def create_module(self, _path, name, template=blank_template):
        self.create_folder(_path, name)

        module_path = os.path.join(_path, name)
        self.create_file(module_path, '__init__.py', template, False)

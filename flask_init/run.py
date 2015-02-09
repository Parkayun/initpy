#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

import six

from .exceptions import PathAlreadyExists
from .templates import *


def create_py(py_path, content):
    with open(py_path, 'w') as py:
        py.write(content)


def main():
    inputs = (
        ('name', 'Input project name: '),
        ('module', 'Input module name (default \'base\'): '),
    )
    values = {}

    for title, question in inputs:
        values[title] = six.moves.input(question)

    values['module'] = values.get('module') or 'base'

    proj_path = os.path.join(os.getcwd(), values['name'])

    try:
        if os.path.exists(proj_path):
           raise PathAlreadyExists

        os.mkdir(proj_path)
        create_py(os.path.join(proj_path, "manager.py"), manager_template)

        os.mkdir(os.path.join(proj_path, "templates"))
        os.mkdir(os.path.join(proj_path, "static"))

        os.mkdir(os.path.join(proj_path, "app"))
        app_path = os.path.join(proj_path, "app")
        create_py(os.path.join(app_path, "__init__.py"), 
                app_init_template.substitute(module=values['module']))

        """
            Support Django style MVC
            TODO: chocie MVC style
        """
        os.mkdir(os.path.join(app_path, values['module']))
        module_path = os.path.join(app_path, values['module'])
        create_py(os.path.join(module_path, "__init__.py"), 
                module_init_template.substitute(module=values['module']))
        create_py(os.path.join(module_path, "views.py"), blank_template)
        create_py(os.path.join(module_path, "models.py"), blank_template)

    except PathAlreadyExists:
        six.print_("Path Already Exists, use another name!")

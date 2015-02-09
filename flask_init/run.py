#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

import six

from .exceptions import *
from .templates import *


def create_folder(_folder_path, _exception):
    if os.path.exists(_folder_path):
        raise _exception
    os.mkdir(_folder_path)


def get_result_and_create_assets(_proj_path):
    result = []

    data = (
        ("templates", TemplatePathAlreadyExists),
        ("static", StaticPathAlreadyExists),
    )

    for folder, exception in data:
        try:
            create_folder(os.path.join(_proj_path, folder), exception)
        except exception:
            error = folder.title() + " folder create skipped (alreay exists)"
            results.append(error)

    return result


def get_result_and_create_module(_app_path, module):
    result = []
    module_path = os.path.join(_app_path, module)
    try:
        if os.path.exists(module_path):
            raise ModulePathAlreadyExists
        os.mkdir(os.path.join(_app_path, module))
    except ModulePathAlreadyExists:
        result.append("Module folder create skipped (already exists)")

    create_py(os.path.join(module_path, "__init__.py"), 
            module_init_template.substitute(module=module))
    create_py(os.path.join(module_path, "views.py"), blank_template)
    create_py(os.path.join(module_path, "models.py"), blank_template)

    return result


def create_py(py_path, content):
    with open(py_path, 'w') as py:
        py.write(content)


def check_name(_name):
    _filter = "!@#$%^&*()-+=[]{}|\"'."
    if len(list(set(list(_name)).intersection(list(_filter)))) > 0:
        return False
    if _name[0].isdigit():
        return False
    return True


def main():
    inputs = (
        ('name', 'Input project name (default is "flask_proj)": '),
        ('module', 'Input module name (default is "base"): '),
    )
    values = {}
    result = []

    for title, question in inputs:
        values[title] = six.moves.input(question)

    try:
        values['name'] = values.get('name') or "flask_proj"
        if not check_name(values['name']):
            raise InvalidProjectName
        values['module'] = values.get('module') or "base"

        proj_path = os.path.join(os.getcwd(), values['name'])

        if os.path.exists(proj_path):
           raise ProjectPathAlreadyExists

        os.mkdir(proj_path)
        create_py(os.path.join(proj_path, "manager.py"), manager_template)

        result.extend(get_result_and_create_assets(proj_path))
        
        """
            Support Django style MVC
            TODO: chocie MVC style
        """
        os.mkdir(os.path.join(proj_path, "app"))
        app_path = os.path.join(proj_path, "app")
        create_py(os.path.join(app_path, "__init__.py"), 
                app_init_template.substitute(module=values['module']))

        result.extend(get_result_and_create_module(app_path, values['module']))

        if len(result) > 0:
            six.print_("\n".join(result))

    except ProjectPathAlreadyExists:
        six.print_("Path Already Exists, use another name!")
    except InvalidProjectName:
        six.print_("Invalid Project Name, use another name!")

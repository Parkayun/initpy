#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

import six

import templates
from .creator import Creator
from .exceptions import InvalidFolderName


def main():
    inputs = (
        ('name', 'Input project name (default is "flask_proj"): '),
        ('module', 'Input module name (default is "common"): '),
    )
    values = {}

    for title, question in inputs:
        values[title] = six.moves.input(question)

    values['name'] = values.get('name') or "flask_proj"
    values['module'] = values.get('module') or "common"

    creator = Creator(os.getcwd())

    try:
        creator.create_folder(creator.root_path, values['name'])
        proj_path = os.path.join(creator.root_path, values['name'])
        creator.create_file(proj_path, "manage.py", templates.manager)
    except InvalidFolderName:
        six.print_("\nInvalid Project Name, use another name!")

    creator.create_folder(proj_path, "requirements")
    creator.create_file(os.path.join(proj_path, "requirements"), "dev.txt",
            templates.requirements)

    creator.create_module(proj_path, "app",
            templates.app_init.substitute(module=values['module']))
    app_path = os.path.join(proj_path, "app")

    creator.create_folder(app_path, "templates")
    template_path = os.path.join(app_path, "templates")
    creator.create_file(template_path, "base.html", templates.base_html)
    creator.create_folder(template_path, values['module'])
    creator.create_file(os.path.join(template_path, values['module']),
        "index.html", templates.module_html)

    creator.create_folder(app_path, "static")
    creator.create_module(app_path, values['module'],
            templates.module_init.substitute(module=values['module']))
    module_path = os.path.join(app_path, values['module'])

    creator.create_file(module_path, "views.py",
            templates.module_views.substitute(module=values['module']))
    creator.create_file(module_path, "models.py", templates.blank)

    six.print_("\n".join(creator.errors))

    six.print_("You can install package "
               "\"pip install -r requirements/dev.txt\"")
    six.print_("You can run \"python manage.py run\"")


if __name__ == '__main__':
    main()

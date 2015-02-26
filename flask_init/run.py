#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

import six

import templates
from .creator import Creator
from .exceptions import InvalidFolderName


def main():
    name = six.moves.input('Input project name (default is "flask_proj"): ')
    name = name or 'flask_proj'
    module = six.moves.input('Input module name (default is "common"): ')
    module = module or 'common'

    creator = Creator(os.getcwd())

    try:
        creator.create_folder(creator.root_path, name)
        proj_path = os.path.join(creator.root_path, name)
    except InvalidFolderName:
        six.print_("\nInvalid Project Name, use another name!")
    else:
        creator.create_file(proj_path, "manage.py", templates.manager)

    creator.create_folder(proj_path, "requirements")
    creator.create_file(os.path.join(proj_path, "requirements"), "dev.txt",
                        templates.requirements)

    app_init = templates.app_init.substitute(module=module)
    creator.create_module(proj_path, "app", app_init)

    app_path = os.path.join(proj_path, "app")
    creator.create_folder(app_path, "templates")

    template_path = os.path.join(app_path, "templates")
    creator.create_file(template_path, "base.html", templates.base_html)
    creator.create_folder(template_path, module)
    creator.create_file(os.path.join(template_path, module),
                        "index.html", templates.module_html)

    module_init = templates.module_init.substitute(module=module)
    creator.create_folder(app_path, "static")
    creator.create_module(app_path, module, module_init)

    module_view = templates.module_views.substitute(module=module)
    module_path = os.path.join(app_path, module)
    creator.create_file(module_path, "views.py", module_view)
    creator.create_file(module_path, "models.py", templates.blank)

    six.print_("\n".join(creator.errors))

    six.print_("You can install package "
               "\"pip install -r requirements/dev.txt\"")
    six.print_("You can run \"python manage.py run\"")


if __name__ == '__main__':
    main()

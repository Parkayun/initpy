#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

import six

from flask_init import templates
from flask_init.creator import Creator
from flask_init.exceptions import InvalidFolderName


def color_input(color, text):
    return six.moves.input(color+text+'\033[0m')


def color_print(color, text):
    six.print_(color+text+'\033[0m')


def main():
    try:
        name = color_input("\033[35m", "> Project name [flask_proj]: ")
        name = name or 'flask_proj'
        module = color_input("\033[35m", "> Module name [common]: ")
        module = module or 'common'
    except KeyboardInterrupt:
        six.print_(""); return

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

    color_print("\033[31m", "\n".join(creator.errors))

    color_print("\033[34m", "Complete!")
    six.print_("You can install package using ", end="")
    color_print("\033[34m", "pip install -r requirements/dev.txt")
    six.print_("You can run using ", end="")
    color_print("\033[34m", "python manage.py run")


if __name__ == '__main__':
    main()

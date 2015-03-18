#!/usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import absolute_import

from os import getcwd
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--flask', '-f', action='store_true')
    parser.add_argument('--tornado-web', '-tw', action='store_true')
    parser.add_argument('name', metavar='name', type=str)
    args = parser.parse_args()

    if args.name != '':
        if args.flask and args.tornado_web:
            from initpy.prompt import color_print
            color_print('Please use one option', 'red')
            parser.print_help()
            return

        if args.flask or args.tornado_web:
            end_message = "Complete!\nYou can install "
            end_message += "\"pip install -r requirments/dev.txt\""

            if args.flask:
                end_message += "\nYou can run \"python manage.py run\""
                from initpy.creator import FlaskCreator
                creator = FlaskCreator(getcwd())
            elif args.tornado_web:
                end_message += "\nYou can run \"python app.py\""
                from initpy.creator import TornadoCreator
                creator = TornadoCreator(getcwd())

            from initpy.prompt import color_input
            module = color_input('Please input base module name [common]: ', 
                    'yellow') or "common"
            creator.create_project(args.name, module)

            from initpy.prompt import color_print
            color_print("\n".join(creator.errors), "red")
            color_print(end_message, "blue")

        else:
            from initpy.creator import Creator
            creator = Creator(getcwd())
            if args.name.endswith('/'):
                try:
                    creator.create_module(creator.root_path, args.name[:-1])
                except IOError:
                    # file exists what contain same name
                    pass
            else:
                extension = ''
                tmpl = ''
                try:
                    extension = args.name.split('.')[-1]
                except IndexError:
                    pass
                if extension == 'py':
                    from initpy.templates import blank
                    tmpl = blank
                creator.create_file(creator.root_path, args.name, tmpl)


if __name__ == '__main__':
    main()

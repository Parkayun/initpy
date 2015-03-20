#!/usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import absolute_import

from os import getcwd, path, mkdir
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--flask', '-f', action='store_true')
    parser.add_argument('--tornado-web', '-tw', action='store_true')
    parser.add_argument('--falcon', '-fc', action='store_true')
    parser.add_argument('--download', '-d', type=str)
    parser.add_argument('name', metavar='name', type=str)
    args = parser.parse_args()

    if args.name != '':
        if args.flask and args.tornado_web and args.falcon and args.download:
            from initpy.prompt import color_print
            color_print('Please use one option', 'red')
            parser.print_help()
            return

        if args.flask or args.tornado_web or args.falcon:
            end_message = "Complete!\nYou can install "
            end_message += "\"pip install -r requirements/dev.txt\""

            if args.flask:
                end_message += "\nYou can run \"python manage.py run\""
                from initpy.creator import FlaskCreator
                creator = FlaskCreator(getcwd())
            elif args.tornado_web:
                end_message += "\nYou can run \"python app.py\""
                from initpy.creator import TornadoCreator
                creator = TornadoCreator(getcwd())
            elif args.falcon:
                end_message += "\nYou can run \"python manage.py\""
                from initpy.creator import FalconCreator
                creator = FalconCreator(getcwd())

            from initpy.prompt import color_input
            module = color_input('Please input base module name [common]: ', 
                    'yellow') or "common"
            creator.create_project(args.name, module)

            from initpy.prompt import color_print
            color_print("\n".join(creator.errors), "red")
            color_print(end_message, "blue")

        elif args.download:
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

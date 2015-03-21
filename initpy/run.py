#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import

from os import getcwd
import argparse

from initpy.prompt import color_print


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--flask', '-f', action='store_true')
    parser.add_argument('--tornado-web', '-tw', action='store_true')
    parser.add_argument('--falcon', '-fc', action='store_true')
    parser.add_argument('--hosted', '-hd', type=str)
    parser.add_argument('--download', '-d', type=str)
    parser.add_argument('name', metavar='name', type=str)
    args = parser.parse_args()

    if args.name != '':
        if args.flask and args.tornado_web and args.falcon and args.download \
                and args.hosted:
            color_print('Please use one option', 'red')
            parser.print_help()
            return

        if args.flask or args.tornado_web or args.falcon:
            end_message = "You can install \"pip install -r requirements/dev.txt\""

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

            color_print("\n".join(creator.errors), "red")
            color_print("Successfully created "+args.name+"!", "blue")
            color_print(end_message, "magenta")

        elif args.download:
            from initpy.creator import downloader
            downloader(args)

        elif args.hosted:
            url = 'https://raw.githubusercontent.com/Parkayun/initpy-index/'
            url += 'master/%s/deatil.json' % args.hosted
            from urllib2 import urlopen, HTTPError
            try:
                res = urlopen(url).read()
                from json import loads
                detail = loads(res.replace('\n', ''))
            except HTTPError:
                color_print("Template not found!", "red")
                return
            except ValueError:
                color_print("This template have a error!", "red")
                return

            args.download = detail['zip']
            color_print("Downloading "+detail['name'], "yellow")
            from initpy.creator import downloader
            downloader(args)
            color_print("Successfully created "+args.name+"!", "blue")

        else:
            from initpy.creator import Creator
            creator = Creator(getcwd())
            if args.name.endswith('/'):
                try:
                    creator.create_module(creator.root_path, args.name[:-1])
                    color_print("Successfully created "+args.name+"!", "blue")
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
                    from initpy.templates.blank import python
                    tmpl = python
                creator.create_file(creator.root_path, args.name, tmpl)
                color_print("Successfully created "+args.name+"!", "blue")


if __name__ == '__main__':
    main()

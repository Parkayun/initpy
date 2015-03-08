#!/usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import absolute_import

from os import getcwd
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--flask', '-f', action='store_true')
    # parser.add_argument('--tornado', '-t', action='store_true')
    parser.add_argument('name', metavar='name', type=str)
    args = parser.parse_args()

    if args.name != '':
        if args.flask:
            from initpy.creator import FlaskCreator
            creator = FlaskCreator(getcwd())
            creator.create_project(args.name, "common")
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

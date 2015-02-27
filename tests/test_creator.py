#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask_init.creator import Creator


def test_file_create(tmpdir):
    file_name = 'test'

    creator = Creator(str(tmpdir.realpath()))

    assert not tmpdir.join(file_name).isfile()
    creator.create_file(creator.root_path, file_name, '')
    assert tmpdir.join(file_name).isfile()

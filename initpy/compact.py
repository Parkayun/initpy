#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys


PY_VER = sys.version_info[0]

if PY_VER == 2:
    from StringIO import StringIO
    input = raw_input
else:
    from io import StringIO
    input = input

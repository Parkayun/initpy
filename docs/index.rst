initpy
======

.. image:: https://pypip.in/v/initpy/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/initpy/
   :alt: Latest Version
.. image:: https://readthedocs.org/projects/initpy/badge/?version=latest
   :target: http://initpy.readthedocs.org/en/latest/
   :alt: Documentation Status

Generate Python Project


Installing
~~~~~~~~~~

initpy is available in `PyPI <http://pypi.python.org/pypi/initpy>`_.

.. sourcecode:: bash

   ~ $ pip install initpy

Install latest works from `Github <https://github.com/Parkayun/initpy>`_.

.. sourcecode:: bash

   ~ $ pip install git+git://github.com/Parkayun/initpy.git


Usage
~~~~~
Create single Python file.

.. sourcecode:: bash

   ~ $ init.py foo.py
   ~ $ cat foo.py
   #!/usr/bin/python
   # -*- coding:utf-8 -*-

Create Python Module.

.. sourcecode:: bash
   
   ~ $ init.py foo/
   ~ $ tree foo/
   foo/
   └── __init__.py

Create Flask project.

.. sourcecode:: bash
   
   ~ $ init.py -f bar
   ~ $ tree bar/
   bar/
    ├── app
    │   ├── __init__.py
    │   ├── common
    │   │   ├── __init__.py
    │   │   ├── models.py
    │   │   └── views.py
    │   ├── static
    │   └── templates
    │       ├── base.html
    │       └── common
    │           └── index.html
    ├── manage.py
    └── requirements
        └── dev.txt

Create Tornado web project.

.. sourcecode:: bash
   
   ~ $ init.py -tw bar
   ~ $ tree bar/
   bar/
    ├── app.py
    ├── handlers
    │   ├── __init__.py
    │   └── common.py
    ├── requirements
    │   └── dev.txt
    └── urls.py

Create Falcon project.

.. sourcecode:: bash

   ~ $ init.py -fc bar
   ~ $ tree bar/
   bar/
    ├── app
    │   ├── __init__.py
    │   ├── resources
    │   │   ├── __init__.py
    │   │   └── common.py
    │   ├── middleware
    │   │   └── __init__.py
    │   └── models
    │       └── __init__.py
    ├── manage.py
    └── requirements
        └── dev.txt


Author and License
~~~~~~~~~~~~~~~~~~

initpy is written by `Ayun Park`_ and distributed under `MIT License`_.

.. _Ayun Park: http://www.parkayun.kr
.. _MIT License: https://github.com/Parkayun/initpy/blob/master/LICENSE

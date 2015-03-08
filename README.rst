initpy
======

Generate `Python`_ project.

.. _Python: https://www.python.org/


Installation
-------------

.. sourcecode:: bash

   ~ $ python setup.py install

or can use pip

.. sourcecode:: bash

   ~ $ pip install initpy


Quick start
-----------
* Create single Python file.
.. sourcecode:: bash

   ~ $ init.py foo.py
   ~ $ cat foo.py
   #!/usr/bin/python
   # -*- coding:utf-8 -*-

* Create Python Module.
.. sourcecode:: bash
   
   ~ $ init.py foo/
   ~ $ tree foo/
   foo/
   └── __init__.py

* Create Flask project.
.. sourcecode:: bash
   
   ~ $ init.py -f bar/
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

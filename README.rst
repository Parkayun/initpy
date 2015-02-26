flask-init
==========

.. image:: https://pypip.in/v/flask-init/badge.svg
    :target: https://pypi.python.org/pypi/flask-init/
    :alt: Latest Version
.. image:: https://readthedocs.org/projects/flask-init/badge/
    :alt: Documentation Status
    :target: http://flask-init.readthedocs.org/en/latest/
.. image:: https://secure.travis-ci.org/Parkayun/flask-init.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/Parkayun/flask-init
.. image:: https://img.shields.io/coveralls/Parkayun/flask-init.svg
   :alt: Coverage Status
   :target: https://coveralls.io/r/Parkayun/flask-init


Generate `Flask` project.

.. _Flask: http://flask.pocoo.org/


Installation
-------------

.. sourcecode:: bash

   ~ $ python setup.py install

or can use pip

.. sourcecode:: bash

   ~ $ pip install flask-init


Quick start
-----------

.. sourcecode:: bash

   ~ $ flask-init
   Input project name (default is "flask_proj"): foo
   Input module name (default is "common"): bar

   You can install package "pip install -r requirements/dev.txt"
   You can run "python manage.py run"
   ~ $ tree foo
   foo
   ├── app
   │   ├── __init__.py
   │   ├── bar
   │   │   ├── __init__.py
   │   │   ├── models.py
   │   │   └── views.py
   │   ├── static
   │   └── templates
   │       ├── base.html
   │       └── bar
   │           └── index.html
   ├── manage.py
   └── requirements
       └── dev.txt
   ~ $ cd foo; pip install -r requirements/dev.txt
   ~ $ python manage.py run

ToDo
----
* Support another mvc folder structure

.. sourcecode:: bash

   ├── app
   │   ├── __init__.py
   │   ├── views
   │   │   ├── __init__.py
   │   │   └── bar.py
   │   ├── models
   │   │   ├── __init__.py
   │   │   └── bar.py

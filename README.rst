flask-init
==========

Generate `Flask` project.

.. _Flask: http://flask.pocoo.org/


Installation
-------------

.. sourcecode:: bash

   ~ $ python setup.py install


Quick start
-----------

.. sourcecode:: bash

   ~ $ flask-init
   Input project name (default is "flask_proj"): foo
   Input module name (default is "common"): bar
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
   └── manager.py

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


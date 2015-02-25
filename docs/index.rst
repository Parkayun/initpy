flask-init
==========

.. image:: https://pypip.in/v/flask-init/badge.svg
    :target: https://pypi.python.org/pypi/flask-init/
    :alt: Latest Version
.. image:: https://secure.travis-ci.org/Parkayun/flask-init.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/Parkayun/flask-init
.. image:: https://img.shields.io/coveralls/Parkayun/flask-init.svg
   :alt: Coverage Status
   :target: https://coveralls.io/r/Parkayun/flask-init

Generate Flask Project


Basic Concepts
~~~~~~~~~~~~~~
flask-init is `Flask`_ project generator and inspired by `django-admin.py`_.

.. _Flask: http://flask.pocoo.org/
.. _django-admin.py: https://docs.djangoproject.com/en/1.7/ref/django-admin/


This package makes `Django`_ style mvc structure, mange.py, requirements, 
templates and static.

.. _Django: https://www.djangoproject.com/


Installing
~~~~~~~~~~

flask-init is available in `PyPI <http://pypi.python.org/pypi/flask-init>`_.

.. sourcecode:: bash

   ~ $ pip install flask-init

Install latest works from `Github <https://github.com/Parkayun/flask-init>`_.

.. sourcecode:: bash

   ~ $ pip install git+git://github.com/Parkayun/flask-init.git


Usage
~~~~~

.. sourcecode:: bash

   ~ $ flask-init
   Input project name (default is "flask_proj"): foo
   Input module name (default is "common"): bar
   
   You can install package "pip install -r requirements/dev.txt"
   You can run "python manage.py run"

After generatred, you can see project structure.

.. sourcecode:: bash

   ~ $ tree foo
   foo
   ├── app
   │   ├── __init__.py
   │   ├── bar
   │   │   ├── __init__.py
   │   │   ├── models.py
   │   │   └── views.py
   │   ├── static
   │   └── templates
   │       ├── base.html
   │       └── bar
   │           └── index.html
   ├── manage.py
   └── requirements
       └── dev.txt

And you can run after install requirement packages.

.. sourcecode:: bash

   ~ $ pip install -r requirements/dev.txt
   ~ $ python manage.py run


Author and License
~~~~~~~~~~~~~~~~~~

flask-init is written by `Ayun Park`_ and distributed under `MIT License`_.

.. _Ayun Park: http://www.parkayun.kr
.. _MIT License: https://github.com/Parkayun/flask-init/blob/master/LICENSE

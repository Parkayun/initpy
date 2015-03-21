initpy
======

.. image:: https://pypip.in/v/initpy/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/initpy/
   :alt: Latest Version
.. image:: https://readthedocs.org/projects/initpy/badge/?version=latest
   :target: http://initpy.readthedocs.org/en/latest/
   :alt: Documentation Status

Generate `Python`_ project.

.. _Python: https://www.python.org/


Installation
------------

.. sourcecode:: bash

   ~ $ python setup.py install

or can use pip

.. sourcecode:: bash

   ~ $ pip install initpy


Quick start
-----------

.. sourcecode:: bash

   ~ $ init.py foo.py             # Create single Python file.
   ~ $ init.py foo/               # Create Python Module.
   ~ $ init.py -f foo             # Create Flask project.
   ~ $ init.py -tw foo            # Create Tornado web project.
   ~ $ init.py -fc foo            # Create Falcon project.
   ~ $ init.py -hd flask foo      # Create project from 3rd-Party template.


More details in `docs <http://initpy.readthedocs.org/en/latest/>`_.
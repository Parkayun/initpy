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


Quick Start
~~~~~~~~~~~

.. sourcecode:: bash

   ~ $ init.py foo.py             # Create single Python file.
   ~ $ init.py foo/               # Create Python Module.
   ~ $ init.py -f foo             # Create Flask project.
   ~ $ init.py -tw foo            # Create Tornado web project.
   ~ $ init.py -fc foo            # Create Falcon project.
   ~ $ init.py -hd flask foo      # Create project from 3rd-Party template.


Options
~~~~~~~

.. toctree::
   :maxdepth: 2

   options/index


3rd-Party Template
~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   3rd_party/index


Author and License
~~~~~~~~~~~~~~~~~~

initpy is written by `Ayun Park`_ and distributed under `MIT License`_.

.. _Ayun Park: http://www.parkayun.kr
.. _MIT License: https://github.com/Parkayun/initpy/blob/master/LICENSE

Create various project
======================

flask
-----

flask option can easily create `Flask <http://flask.pocoo.org/>`_ project.

Can use this option with --flask or -f.

.. sourcecode:: bash

    ~ $ init.py --flask foo
    Please input base module name [common]: bar

    Successfully created foo!
    You can install "pip install -r requirements/dev.txt"
    You can run "python manage.py run"
    ~ $ tree foo/
    foo/
    ├── app
    │   ├── __init__.py
    │   ├── bar
    │   │   ├── __init__.py
    │   │   ├── models.py
    │   │   └── views.py
    │   ├── static
    │   └── templates
    │       ├── bar
    │       │   └── index.html
    │       └── base.html
    ├── manage.py
    └── requirements
        └── dev.txt

tornado web
-----------

tornado web option can easily create `Tornado <http://www.tornadoweb.org/en/stable/>`_ web project.

Can use this option with --tornado-web or -tw.

.. sourcecode:: bash

    ~ $ init.py --tornado-web foo
    Please input base module name [common]: bar

    Successfully created foo!
    You can install "pip install -r requirements/dev.txt"
    You can run "python app.py"
    ~ $ tree foo/
    foo/
    ├── app.py
    ├── handlers
    │   ├── __init__.py
    │   └── bar.py
    ├── requirements
    │   └── dev.txt
    └── urls.py


falcon
------

tornado web option can easily create `falcon <http://falconframework.org/>`_ project.

Can use this option with --falcon or -fc.

.. sourcecode:: bash

    ~ $ init.py --falcon foo
    Please input base module name [common]: bar

    Successfully created foo!
    You can install "pip install -r requirements/dev.txt"
    You can run "python manage.py"
    ~ $ tree foo/
    foo/
    ├── app
    │   ├── __init__.py
    │   ├── middleware
    │   │   └── __init__.py
    │   ├── models
    │   │   ├── __init__.py
    │   │   └── bar.py
    │   └── resources
    │       ├── __init__.py
    │       └── bar.py
    ├── manage.py
    └── requirements
        └── dev.txt


hosted
------

hosted option can create project from 3rd-Party template.

Can use this option with --hosted or -hd.

.. sourcecode:: bash

   ~ $ init.py --hosted flask foo
   Downloading flask
   Successfully created foo!

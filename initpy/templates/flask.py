#!/usr/bin/env python
# -*- coding:utf-8 -*-
from string import Template


app_init = Template("""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)


def create_app():
    from ${module} import ${module}_blueprint
    app.register_blueprint(${module}_blueprint)
    return app
""".strip())


manager = """
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.script import Manager

# from werkzeug.contrib.fixers import ProxyFix

from app import create_app


app = create_app()
# app.wsgi_app = ProxyFix(app.wsgi_app)
manager = Manager(app)

@manager.command
def run():
    app.run()

if __name__ == "__main__":
    manager.run()
""".strip()


module_init = Template("""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint

${module}_blueprint = Blueprint('${module}', __name__)

from . import views
""".strip())


module_views = Template("""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template

from . import ${module}_blueprint


@${module}_blueprint.route('/')
def index():
    return render_template('${module}/index.html')
""".strip())


module_html = """
{% extends "base.html" %}

{% block title %}flask-init{% endblock %}

{% block body %}
<h1>Hello Word</h1>
{% endblock %}
""".strip()

base_html = """
<!DOCTYPE html>
<html>
    <meta charset="utf-8">
    <head>{% block head %}{% endblock %}</head>
</html>
<body>
{% block body %}
{% endblock %}
</body>
</html>
""".strip()

requirements = """
Flask
Flask-Script
""".strip()
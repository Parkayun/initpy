#!/usr/bin/python
# -*- coding: utf-8 -*-
from string import Template


app_init = Template("""
#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)


def create_app():
    from ${module} import ${module}_blueprint
    app.register_blueprint(${module}_blueprint)
    return app
""".strip())


blank = """
#!/usr/bin/python
# -*- coding:utf-8 -*-
""".strip()


manager = """
#!/usr/bin/python
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
#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint

${module}_blueprint = Blueprint('${module}', __name__)

from . import views
""".strip())


module_views = Template("""
#!/usr/bin/python
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

flask_requirements = """
Flask
Flask-Script
""".strip()


tornado_app = """
#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options

from urls import url_patterns


class TornadoApplication(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns)


def main():
    try:
        port = int(sys.argv[1])
    except:
        port = 8080

    app = TornadoApplication()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(port)
    tornado.options.parse_command_line()
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
""".strip()


tornado_handler = """
#!/usr/bin/python
# -*- coding:utf-8 -*-
import tornado.web


class IndexHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        self.write('Hello World')
        self.finish()
""".strip()


tornado_urls = Template("""
#!/usr/bin/python
# -*- coding:utf-8 -*-
from handlers.${module} import IndexHandler


url_patterns = [
    (r'^/$$', IndexHandler),
]
""".strip())


tornado_requirements = """
tornado
""".strip()

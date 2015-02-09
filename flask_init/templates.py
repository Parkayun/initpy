#!/usr/bin/python
# -*- coding: utf-8 -*-
from string import Template


app_init_template = Template("""
#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)


def create_app():
    from ${module} import ${module}_blueprint
    app.register_blueprint(${module}_blueprint)
    return app
""".strip())


blank_template = """
#!/usr/bin/python
# -*- coding:utf-8 -*-
""".strip()


manager_template = """
#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask.ext.script import Manager

from werkzeug.contrib.fixers import ProxyFix

from app import create_app


app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)
manager = Manager(app)

@manager.command
def run():
    app.run()

if __name__ == "__main__":
    manager.run()
""".strip()


module_init_template = Template("""
#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint

${module}_blueprint = Blueprint('${module}', __name__)

from . import views
""".strip())


base_html_template = """
<!DOCTYPE html>
<html>
    <meta charset="utf-8">
    <head>{% block head %}</head>
</html>
<body>
{% block body %}
{% endblock %}
</body>
</html>
""".strip()

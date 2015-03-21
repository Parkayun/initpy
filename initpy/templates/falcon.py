#!/usr/bin/env python
# -*- coding:utf-8 -*-
from string import Template


app_init = Template("""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import falcon

# from .middleware import *
from .resources import ${module_title}Resource

${module}Resource = ${module_title}Resource()


def create_app():
    app = falcon.API(middleware=[])

    app.add_route('/', ${module}Resource)

    return app
""".strip())


manager = """
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wsgiref import simple_server

from app import create_app


# Set up falcon api
app = application = create_app()


if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 5000, app)
    httpd.serve_forever()
""".strip()


resource_init = Template("""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .${module} import ${module_title}Resource
""".strip())


resource_controller = Template("""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import falcon


class ${module_title}Resource(object):
    def __init__(self):
        pass

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Hello World'

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Hello World'
""".strip())


requirements = """
falcon
""".strip()

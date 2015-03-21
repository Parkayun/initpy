#!/usr/bin/env python
# -*- coding:utf-8 -*-
from string import Template


tornado_app = """
#!/usr/bin/env python
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
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web


class IndexHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        self.write('Hello World')
        self.finish()
""".strip()


tornado_urls = Template("""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from handlers.${module} import IndexHandler


url_patterns = [
    (r'^/$$', IndexHandler),
]
""".strip())


requirements = """
tornado
""".strip()

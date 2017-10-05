"""
tornado模块
https://github.com/tornadoweb/tornado
"""
import tornado.ioloop
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    pass

class Application:
    def __init__(self):
        self.views = []

    def add_view(self, view_name, handler):
        self.views.append((view_name, handler))

    def start(self, port):
        self.application = tornado.web.Application(self.views)
        self.application.listen(port)
        tornado.ioloop.IOLoop.instance().start()

    def close(self):
        pass
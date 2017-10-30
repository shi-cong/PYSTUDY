"""
tornado模块
https://github.com/tornadoweb/tornado
"""
import tornado.ioloop
import tornado.web
from PYSTUDY.modulelib import is_subclass

class BaseHandler(tornado.web.RequestHandler):
    """
    对requesthandler进行封装
    """
    def get_param(self, name, default):
        """
        获取get或者post表单参数
        :param name: 参数名
        :param default: 默认值
        :return: 参数的值
        """
        return self.get_argument(name, default)


class Application:
    def __init__(self):
        self.views = [] # 路由列表

    def add_view(self, view_name, handler):
        """
        增加handler
        :param view_name: 路由
        :param handler: 处理类
        :return:
        """
        # 如果不是BaseHandler的子类则不加入
        if is_subclass(handler, BaseHandler):
            self.views.append((view_name, handler))

    def add_template_path(self, path):
        """
        增加模版文件路径
        :param path: 路径 
        :return:
        """
        self.templatePath = path

    def add_static_path(self, path):
        """
        增加静态文件路径
        :param path: 路径 
        :return:
        """
        self.staticPath= path

    def start(self, port):
        """
        启动服务器
        :param port: 端口号
        :return:
        """
        self.application = tornado.web.Application(self.views, 
                template_path=self.templatePath, 
                static_path=self.staticPath)
        self.application.listen(port)
        tornado.ioloop.IOLoop.instance().start()

    def close(self):
        """
        关闭服务器
        :return:
        """
        pass

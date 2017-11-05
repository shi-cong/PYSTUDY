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

    def get_body(self):
        """如果是json数据post，则用这个方法获取
        :return: 返回到数据是bytes类型
        """
        return self.request.body

    def get_client_ip(self):
        """
        获取客户端ip
        """
        return self.request.remote_ip

    def get_client_headers(self):
        """
        获取请求头
        """
        return self.request.headers

    def raise_403_error(self):
        """阻止访问"""
        raise tornado.web.HTTPError(403)

    def raise_406_error(self):
        """请求的资源的内容特性无法满足请求头中的条件，因而无法生成响应实体"""
        raise tornado.web.HTTPError(406)


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

    def set_template_path(self, path):
        """
        增加模版文件路径
        :param path: 路径 
        :return:
        """
        self.templatePath = path

    def set_static_path(self, path):
        """
        增加静态文件路径
        :param path: 路径 
        :return:
        """
        self.staticPath = path

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

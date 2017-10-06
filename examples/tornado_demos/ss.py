"""
搜索服务
"""

from examples.mysqllib_demos import ss_db
from shicong.tornadolib import BaseHandler, Application


class SSHandler(BaseHandler):
    def get(self):
        """
        搜索关键字并返回搜索结果
        :param keyword: 关键字
        :param page: 页数
        :return:
        """
        # 获得get请求参数
        keyword = self.get_param('keyword', '') # 关键字
        page = self.get_param('page', 1) # 页数
        items = ss_db.get(keyword, page) # 搜索结果

        self.write(str(items))


app = Application()
app.add_view(r'/', handler=SSHandler)
app.start(8000)
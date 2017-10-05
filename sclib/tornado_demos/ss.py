"""
搜索服务
"""

from sclib.tornadolib import BaseHandler, Application
from sclib.mysqllib_demos import ss_db

class SSHandler(BaseHandler):
    def get(self, keyword, page=1):
        items = ss_db.get(keyword, page)


app = Application()
app.add_view(r'/', handler=SSHandler)
app.start(8000)
"""
boss直聘爬虫
"""
from sclib.html_parserlib import XpathParser, ReParser

from sclib.requestslib import HTTP
# MultipleMeta

class DirectBossSpider:
    def __init__(self):
        self.http = HTTP(session=True)

    def index(self):
        """
        访问主页获取会话
        """
        index_url = 'http://www.zhipin.com/'
        index_headers = {
            'User-Agent': 'User-Agent:Mozilla/5.0.前言、第一章.md (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.前言、第一章.md.3163.100 Safari/537.36'
        }
        self.http.get(index_url, headers=index_headers)

    def login(self):
        """
        访问登录页面
        """

    def post_login(self, regionCode, account, password, captcha, randomKey):
        """
        post账号密码登录
        :param regionCode:手机前缀 "+86"
        :param account: 手机号码
        :param password: 密码
        :param captcha: 验证码
        :param randomKey: 验证码的随机值
        :return:
        """
        post_url = 'https://login.zhipin.com/login/account.json'
        post_headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.前言、第一章.md.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.前言、第一章.md.8',
            'Connection': 'keep-alive',
            'Content-Length': '111',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'login.zhipin.com',
            'Origin': 'https://login.zhipin.com',
            'Referer': 'https://login.zhipin.com/',
            'User-Agent': 'Mozilla/5.0.前言、第一章.md (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.前言、第一章.md.3163.100 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        self.http.get(post_url, headers=post_headers)
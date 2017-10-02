from sclib.html_parserlib import XpathParser, ReParser
from sclib.requestslib import HTTP

class JiaYuanSpider:
    """
    世纪佳缘爬虫
    主要功能为了获取一些女性的数据来测试k-NN算法的精确度
    爬虫逻辑是：post登陆，登陆跳转，访问用户主页，访问搜索页面
    """
    def __init__(self):
        self.http = HTTP(session=True)

    def do_login(self):
        """
        post登陆
        :return: 登陆跳转的url
        """
        url = 'https://passport.jiayuan.com/dologin.php?host=www.jiayuan.com&new_header=1&channel=index'
        headers = {
            'Host': 'passport.jiayuan.com',
            'Content-Length': '60',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://www.jiayuan.com',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://www.jiayuan.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        }
        form_data = {
            'channel':'200',
            'position':'101',
            'name':'15800223273',
            'password':'sc5201314',
        }
        text, headers, cookies, history = self.http.post(url, headers=headers, form_data=form_data)
        print(text)
        print('-----------------')

        rp = ReParser("\('.*'\)")
        lj_url = rp.compute(text)[2:-2]
        return lj_url

    def login_jump(self, url):
        """
        登陆跳转请求
        :param url: 登陆跳转url
        :return:
        """
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
            'Host':'www.jiayuan.com',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }
        text, headers, cookies, history = self.http.get(url, headers=headers)
        print(text)
        print('-----------------')

    def usercp(self):
        """
        访问用户主页
        :return:
        """
        usercp_url = 'http://usercp.jiayuan.com/?from=login'
        headers = {
            'Host': 'www.jiayuan.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        }
        text, headers, cookies, history = self.http.get(usercp_url, headers=headers)
        print(text)
        print('------------------')

    def search_v2(self):
        """
        访问搜索主页更新session
        :return:
        """
        search_url = 'http://search.jiayuan.com/v2/'
        headers = {
            'Host': 'search.jiayuan.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://usercp.jiayuan.com/?from=login',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        }
        text, headers, cookies, history = self.http.get(search_url, headers=headers)

    def post_search_v2(self, page=1):
        request_url = 'http://search.jiayuan.com/v2/search_v2.php'
        request_headers = {
            'Host': 'search.jiayuan.com',
            'Connection': 'keep-alive',
            'Content-Length': '129',
            'Accept': '*/*',
            'Origin': 'http://search.jiayuan.com',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://search.jiayuan.com/v2/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        }
        form_data = {
            'sex':'f',
            'key':'',
            'stc':'1:33,2:20.28,3:155.170,23:1',
            'sn':'default',
            'sv':'1',
            'p':str(page),
            'f':'',
            'listStyle':'bigPhoto',
            'pri_uid':'168965396',
            'jsversion':'v5',
        }
        text, headers, cookies, history = self.http.post(request_url, headers=request_headers, form_data=form_data)
        print(text)


def main():
    jys = JiaYuanSpider()
    lj_url = jys.do_login()
    jys.login_jump(lj_url)
    jys.usercp()
    jys.search_v2()
    for page in range(11):
        jys.post_search_v2(page+1)


main()
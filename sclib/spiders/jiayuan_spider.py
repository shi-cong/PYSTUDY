from sclib.html_parserlib import XpathParser, ReParser
from sclib.requestslib import HTTP
from sclib.jsonlib import loads
from threading import Thread, active_count
import time
from sclib.mysqllib import MYSQLPool


class JiaYuanSpider:
    """
    世纪佳缘爬虫
    主要功能为了获取一些女性的数据来测试k-NN算法的精确度
    爬虫逻辑是：post登陆，登陆跳转，访问用户主页，访问搜索页面
    """
    def __init__(self):
        self.http = HTTP(session=True)
        self.mysql_pool = MYSQLPool(20,
            **dict(host='192.168.80.4',
                 user='jiayuan',
                 password='123456',
                 db='jiayuan',
                 charset='utf8mb4'))

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
        rp = ReParser('#{.*}#')
        content = rp.compute(text)[1:-1]
        print(content)
        data = loads(content)
        if page == 1:
            self.page_total = data['pageTotal']
        user_info = data['userInfo']

        '''
        {
            "uid": 167911957, 
            "realUid": 168911957, 
            "nickname": "踏月", 
            "sex": "女", 
            "sexValue": "f", 
            "randAttr": "formal", 
            "marriage": "未婚", 
            "height": "160", 
            "education": "本科", 
            "income": null, 
            "work_location": "宁波", 
            "work_sublocation": "宁波", 
            "age": 24, 
            "image": "http://at4.jyimg.com/f0/1b/eedc8bd6dce5e37e1dffb0e37c79/eedc8bd6d_1_avatar_p.jpg", 
            "count": "14291", 
            "online": 0, 
            "randTag": "<span>160cm</span>", 
            "randListTag": "<span>160cm</span>", 
            "userIcon": "<i title=手机认证 class=tel></i>", 
            "helloUrl": "http://www.jiayuan.com/msg/hello.php?type=20&randomfrom=4&uhash=f0eedc8bd6dce5e37e1dffb0e37c791b", 
            "sendMsgUrl": "http://www.jiayuan.com/msg/send.php?uhash=f0eedc8bd6dce5e37e1dffb0e37c791b", 
            "shortnote": "我是一个诚信的人 ，爱好广泛的我，喜欢健身,麦霸。", 
            "matchCondition": "23-31岁,160-185cm,浙江,宁波"
        }
        '''
        sql = 'insert into userInfo values'
        args = []
        uil = len(user_info)  - 1
        count = 0

        for ui in user_info:
            if ui['marriage'] == '未婚':
                ui['marriage'] = 0
            else:
                ui['marriage'] = 1
            if ui['sex'] == '女':
                ui['sex'] = 0
            elif ui['sex'] == '男':
                ui['sex'] = 1
            else:
                ui['sex'] = 2
            
            sql += "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            if count != uil:
                sql += ', '
            count += 1
            args += [ui['uid'], ui['nickname'], ui['sex'], ui['marriage'], ui['height'], ui['education'],
                        ui['work_location'], ui['age'], ui['image'], ui['shortnote'], ui['matchCondition']]

        self.mysql_pool.execute(sql, args)



def main():
    jys = JiaYuanSpider()
    lj_url = jys.do_login()
    jys.login_jump(lj_url)
    jys.usercp()
    jys.search_v2()
    jys.post_search_v2()
    page = 2
    while page <= jys.page_total:
        if active_count() <= 10:
            Thread(target=jys.post_search_v2, args=(page, )).start()
            # jys.post_search_v2(page)
            page += 1
        else:
            time.sleep(2)
            continue


main()
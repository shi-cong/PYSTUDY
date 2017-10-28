"""
拉钩职位职位获取api
"""
from PYSTUDY.net.requestslib import HTTP
from PYSTUDY.jsonlib import loads
from PYSTUDY.randomlib import random_user_agent
from PYSTUDY.encodelib import encode_uri


class LagouSpider:
    def __init__(self):
        self.http = HTTP(session=True)

    def index(self):
        """获取jsessionid"""
        url = 'https://www.lagou.com/'
        headers = {
            'Host': 'www.lagou.com',
            'Cache-Control': 'max-age=0',
            'user-agent': random_user_agent(),
            'Upgrade-Insecure-Requests': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        }
        t, h, c, hi = self.http.get(url, headers=headers)
        print('获取的jsessionid:', c)

    def list(self, keyword='python', location='深圳'):
        """获取一些cookie"""
        url = 'http://www.lagou.com/jobs/list_' + keyword
        headers = {
            'Host': 'www.lagou.com',
            'Content-Length': '26',
            'Origin': 'https://www.lagou.com',
            'X-Anit-Forge-Code': '0',
            'User-Agent': random_user_agent(),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'X-Anit-Forge-Token': 'None',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Referer': 'https://www.lagou.com/',
        }

        query_params = {
            'city': location,
            'cl': 'false',
            'fromSearch': 'true',
            'labelWords':'',
            'suginput':''
        }
        t, h, c, hi = self.http.get(url, headers=headers, params=query_params, timeout=60)
        print(c)


    def pagnation(self, location, keyword='python', page=1, first=True):
        url = 'https://www.lagou.com/jobs/positionAjax.json'
        headers = {
            'Host': 'www.lagou.com',
            'Content-Length': '100' if page==1 else '200',
            'Origin': 'https://www.lagou.com',
            'X-Anit-Forge-Code': '0',
            'User-Agent': random_user_agent(),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'X-Anit-Forge-Token': 'None',
            # 'Referer': 'https://www.lagou.com/jobs/list_' + keyword + '?labelWords=&fromSearch=true&suginput=',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        }
        query_params = None
        if page == 1:
            query_params = {
                'px': 'new',
                'city': location,
                'needAddtionalResult': 'false',
                'isSchoolJob': '0',
            }
        else:
            query_params = {
                'city': location,
                'needAddtionalResult': 'false',
                'isSchoolJob': '0',
            }

        form_data = {
            'first': 'true' if first else 'false',
            'pn': page,
            'kd': keyword
        }

        cookies = {
            'index_location_city': encode_uri(location),
            'TG-TRACK-CODE': 'index_search',
        }
        t, h, c, hi = self.http.post(url, headers=headers, form_data=form_data, cookies=cookies)
        jobj = loads(t)
        print(jobj)
        # 获取总职位数
        self.total_count = jobj['content']['positionResult']['totalCount']

        # 获取总页数
        self.total_pages = self.total_count // 15 if self.total_count % 15 == 0 else self.total_count // 15 + 1

        return jobj['positionResult']['result']


def get_job_by_keyword(keyword):
    """
    这里的Location没有用，不管怎么试和抓包都没用。这个程序只能抓取全国的关于关键字搜索的职位。
    如果封了IP,那就没办法了。
    :param keyword:  关键字
    :return: 返回一个生成器关于职位的
    """
    ls = LagouSpider()
    ls.index()

    ls.list(keyword='python')

    ls.pagnation(location='深圳', keyword='python', page=1, first=True)
    print(ls.total_count)
    print(ls.total_pages)

    for i in range(2, ls.total_pages+1):
        yield ls.pagnation(location='深圳', keyword=keyword, page=i, first=False)

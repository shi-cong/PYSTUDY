"""
gpsspgapi封装
"""
from PYSTUDY.html_parserlib import ReParser
from PYSTUDY.net.requestslib import HTTP
from PYSTUDY.timelib import get_current_timestamp
from PYSTUDY.randomlib import random_user_agent


def geo(*params):
    """
    根据经纬度后去地址
    :param params: 经纬度
    :return: 地址字符串
    """
    api = 'http://www.gpsspg.com/apis/maps/geo/'
    headers = {
        'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
        'Cookie':'ARRAffinity=7996acd7385beb55da51ad553ab9df60d6b742a8d0840faa612d0bd27f840017; Hm_lvt_15b1a40a8d25f43208adae1c1e12a514=1507564728; Hm_lpvt_15b1a40a8d25f43208adae1c1e12a514=1507564728; AJSTAT_ok_pages=1; AJSTAT_ok_times=1',
        'Host':'www.gpsspg.com',
        'Referer':'http://www.gpsspg.com/iframe/maps/qq_161128.htm?mapi=2',
        'User-Agent': random_user_agent(),
        'X-Requested-With':'XMLHttpRequest',
    }
    query_params = {
        'output': 'jsonp',
        'lat': params[0],
        'lng': params[1],
        'type': '0',
        'callback': 'jQuery110207091189337888508_1507564728439',
        '_': int(get_current_timestamp()),
    }
    http = HTTP()
    t, h, c, hi, s = http.get(api, headers=headers, params=query_params)
    rp = ReParser()
    real_data = rp.compute(r'address":".*","rids', t).replace('address":"', '').replace('","rids', '')
    return real_data

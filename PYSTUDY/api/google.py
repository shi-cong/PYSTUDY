"""
google api 模块
"""
from PYSTUDY.net.requestslib import HTTP
from PYSTUDY.randomlib import random_user_agent

def geocode(*params):
    """
    遗憾的是拥有GFW的存在，导致本代码无法运行和测试。
    :param params:
    :return:
    """
    http = HTTP()
    api = 'https://maps.google.com/maps/api/geocode/xml'
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control':'max-age=0',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent': random_user_agent()
    }
    print(','.join(params))
    query_params = {
        'latlng': ','.join(params),
        'language': 'zh-CN',
        'sensor': 'false'
    }
    t, h, c, hi = http.get(api, headers=headers, params=query_params)
    return t

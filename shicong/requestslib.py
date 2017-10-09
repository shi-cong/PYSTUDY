"""
requests模块
"""
import requests
from collections import OrderedDict
from requests.utils import dict_from_cookiejar


class HTTP(object):
    """
    requests深度封装
    """

    def __init__(self, session=False):
        """
        初始化HTTP
        :param session: 决定是否使用SESSION会话
        """
        if session:
            self.session = requests.Session()
            # 设置连接池为100
            adapter = requests.adapters.HTTPAdapter(
                pool_connections=100, pool_maxsize=100)
            self.session.mount('http://', adapter)
            self.session.mount('https://', adapter)
        else:
            self.session = None

    def close(self):
        """
        关闭session，减轻服务器的压力
        :return:
        """
        if self.session:
            self.session.close()

    def get_session_cookie(self):
        """
        获取session的cookies
        :return:
        """
        if self.session:
            return dict_from_cookiejar(self.session.cookies)

    def __select(self, method, url, headers=None, cookies=None, timeout=30, verify=False, proxies=None,
                 allow_redirects=True, encoding='utf-8', params=None, form_data=None):
        """
        对http动作的封装，当传递get，则模拟http get请求，
        当传递post, 则模拟http post请求
        :param method: 'get' or 'post'
        :param url: 访问Url
        :param headers: 请求头
        :param cookies: 请求cookies
        :param timeout: 超时时间
        :param verify: ssl验证
        :param proxies: 代理
        :param allow_redirects: 是否允许重定向
        :param encoding: 返回的html编码
        :param params: 查询请求参数
        :param form_data: 如果是post请求则需要提供有表单提交则需要有这个
        :return: html, 响应头，响应cookie，访问历史
        """
        r = None
        if method == 'get':
            if self.session:
                r = self.session.get(url, headers=OrderedDict(headers), cookies=cookies, timeout=timeout,
                                     verify=verify, proxies=proxies, allow_redirects=allow_redirects, params=params)
            else:
                r = requests.get(url, headers=OrderedDict(headers), cookies=cookies, timeout=timeout, verify=verify,
                                 proxies=proxies, allow_redirects=allow_redirects, params=params)
        elif method == 'post':
            if self.session:
                r = self.session.post(url, headers=OrderedDict(headers), cookies=cookies, timeout=timeout,
                                      data=form_data, verify=verify, proxies=proxies, allow_redirects=allow_redirects,
                                      params=params)
            else:
                r = requests.post(url, headers=OrderedDict(headers), cookies=cookies, timeout=timeout, data=form_data,
                                  verify=verify, proxies=proxies, allow_redirects=allow_redirects, params=params)

        # 若http状态码如果不正常则抛出异常
        r.raise_for_status()
        r.encoding = encoding  # 设置html编码
        return r.text, r.headers, dict_from_cookiejar(r.cookies), r.history

    def get(self, url, headers=None, cookies=None, timeout=30, verify=False, proxies=None, allow_redirects=True,
            encoding='utf-8', params=None):
        """
        模拟http get请求
        :param url: 访问Url
        :param headers: 请求头
        :param cookies: 请求cookies
        :param timeout: 超时时间
        :param verify: ssl验证
        :param proxies: 代理
        :param allow_redirects: 是否允许重定向
        :param encoding: 返回的html编码
        :param params: 查询请求参数
        :return: html, 响应头，响应cookie，访问历史
        """
        return self.__select('get', url, headers=OrderedDict(headers), cookies=cookies, timeout=timeout, verify=verify,
                             proxies=proxies, allow_redirects=allow_redirects, encoding=encoding, params=params)

    def get_img(self, url, headers=None, cookies=None, timeout=30, verify=False, proxies=None, allow_redirects=True,
                params=None):
        """
        get方式获取 img 二进制信息
        :param url: 访问Url
        :param headers: 请求头
        :param cookies: 请求cookies
        :param timeout: 超时时间
        :param verify: ssl验证
        :param proxies: 代理
        :param allow_redirects: 是否允许重定向
        :param encoding: 返回的html编码s
        :param params: 查询请求参数
        :return: 二进制图片数据
        """
        if self.session:
            r = self.session.get(url, headers=OrderedDict(headers), cookies=cookies, timeout=timeout, verify=verify,
                                 proxies=proxies, allow_redirects=allow_redirects, params=params)
        else:
            r = requests.get(url, headers=OrderedDict(headers), cookies=cookies, timeout=timeout, verify=verify,
                             proxies=proxies, allow_redirects=allow_redirects, params=params)
        r.raise_for_status()
        return r.content

    def post(self, url, headers=None, cookies=None, timeout=30, form_data=None, verify=False, proxies=None,
             allow_redirects=True, encoding='utf-8', params=None):
        """
        模拟http post请求
        :param url: 访问Url
        :param headers: 请求头
        :param cookies: 请求cookies
        :param timeout: 超时时间
        :param verify: ssl验证
        :param proxies: 代理
        :param allow_redirects: 是否允许重定向
        :param encoding: 返回的html编码
        :param params: 查询请求参数
        :return: html, 响应头，响应cookie，访问历史
        """
        return self.__select('post', url, headers=OrderedDict(headers), cookies=cookies, timeout=timeout,
                             form_data=form_data, verify=verify, proxies=proxies, allow_redirects=allow_redirects,
                             encoding=encoding, params=params)

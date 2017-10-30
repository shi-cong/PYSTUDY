"""
html解析模块
"""
from scrapy.selector import Selector
import re


class XpathParser(object):
    """
    xpath类封装
    """
    def __init__(self, text):
        self.res = Selector(text=text)

    def xpath(self, text):
        return self.res.xpath(text)


class Link(object):
    """
    链接类
    """
    def __init__(self, text, url):
        self.text = text
        self.url = url


class LinksParser(XpathParser):
    """
    用于解析页面上所有的链接的类,
    """
    def links(self):
        """
        解析页面上所有的链接并返回一个生成器
        """
        ass = self.xpath('//a')
        for a in ass:
            text = a.xpath('./text()').extract_first()
            url = a.xpath('./@href').extract_first()
            link = Link(text, url)
            yield link


class ReParser(object):
    '''
    正则表达式解析封装
    '''
    def compute(self, re_text, text):
        match = re.compile(re_text)
        m = match.search(text) 
        return m.group() if m else None

    def replace(self, re_text, replace_str, text):
        """
        正则表达式替换
        :param re_text: 正则表达式
        :param replace_str: 替换字符串
        :param text: 搜索文档
        :return: 替换后的字符串
        """
        return re.sub(re_text, replace_str, text)

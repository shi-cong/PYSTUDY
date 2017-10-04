"""
html解析模块
"""
from scrapy.selector import Selector
import re


class XpathParser(object):
    def __init__(self, text):
        self.res = Selector(text=text)

    def xpath(self, text):
        return self.res.xpath(text)


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

# -*- coding: utf-8 -*-
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

    def __init__(self, re_text):
        self.match = re.compile(re_text)

    def compute(self, text):
        m = self.match.search(text)
        return m.group() if m else None

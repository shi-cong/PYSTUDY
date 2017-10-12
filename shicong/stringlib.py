"""
stirng模块
"""

def endswith(text, end_str):
    """
    判断字符串是否以某一个字符串结尾
    :param text: 数据
    :param end_str: 关键字
    :return: True or False
    """
    return text.endswith(end_str)

def join(strs, join_str):
    """
    拼接字符串
    :param strs:  字符换列表
    :param join_str: 拼接字符串名称
    :return: 拼接的字符串
    """
    return join_str.join(strs)

def count(text, keyword):
    """
    获取keyword在text中的个数
    :param text: 文章
    :param keyword: 字符串
    :return: 个数
    """
    return text.count(keyword)

def split(text, keyword):
    """
    以制定关键字分割text
    :param text: 数据
    :param keyword: 关键字
    :return: 分割的字符串列表
    """
    return text.split(keyword)


def rsplit(text, keyword, c):
    """
    从右边开始分割字符串
    :param text: 要分割的字符串
    :param keyword: 关键字
    :param c: 分割次数
    :return: 分割的数组
    """
    return text.rsplit(keyword, c)
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


def to_bytes(s):
    """
    将字符串转换成字节数组
    :param s: 要转换成字节数组的字符串
    :return: 转换成字节数组的字符串
    """
    if bytes != str:
        if type(s) == str:
            return s.encode('utf-8')
    return s


def to_str(s):
    """
    将字节数组转成成字符串
    :param s: 字节数组
    :return: 字符串
    """
    if bytes != str:
        """
        这里的比较在python2中是True，在Python3中是False
        """
        if type(s) == bytes:
            return s.decode('utf-8')
    return s

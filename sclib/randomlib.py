# -*- coding: utf-8 -*-

import random
import string


def random_str(n=20):
    """
    随机生成一串密码
    :param n: 密码的长度，默认为20
    :return: 长度为n的随机字符串
    """
    return ''.join(random.sample(string.ascii_letters + string.digits, n))

def random_small_number():
    """
    随机生成一个小数
    :return: 返回小数
    """
    return random.random()

if __name__ == '__main__':
    print(random_str())

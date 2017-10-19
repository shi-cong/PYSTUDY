"""
random随机数封装
"""

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


def random_set(n=1, elements=[]):
    """
    假定集合strs，从中随机取n个元素作为输出
    :param n:
    :param elements:
    :return: 取出随机的集合
    """
    return random.sample(elements, n)


def random_int(left=0, right=1):
    """
    随机从闭区间[left, right]中返回一个整数
    :param left: 区间的左边半径
    :param right: 区间的右边半径
    :return: 随机的整数
    """
    return random.randint(left, right)


def random_float(left=0, right=1):
    """
    随机从闭区间[left, right]中返回一个实数
    :param left: 区间的左边半径
    :param right: 区间的右边半径
    :return: 随机的实数
    """
    return random.uniform(left, right)

def random_user_agent():
    """
    随机一个user-agent
    :return:
    """
    ua_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    ]
    return random_set(1, ua_list)[0]

if __name__ == '__main__':
    print(random_str())

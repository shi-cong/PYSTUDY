"""
时间操作模块
"""
import time


def func_runtime(callback):
    """
    测试函数执行的时间
    :param callback: 函数
    :return: 时间
    """
    now = time.time()
    print('%s - start: %f' % (callback, now))
    callback()
    now = time.time() - now
    print('%s - spent: %f Second' % (callback, now))


def timestamp_to_time(timestamp):
    """
    时间戳转时间字符串
    :param timestamp: 时间戳
    :return: 时间字符串
    """
    x = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', x)


def time_to_timestamp(time_str):
    """
    时间字符串转时间戳
    :param time_str: 时间字符串
    :return: 时间戳
    """
    x = time.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    return time.mktime(x)


def get_current_timestamp():
    """
    获取当前的时间戳
    :return: 时间戳
    """
    return time.time()

def sleep(t):
    time.sleep(t)

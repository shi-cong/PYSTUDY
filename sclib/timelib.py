# -*- coding: utf-8 -*-
import time


def func_runtime(callback):
    now = time.time()
    print('%s - start: %f' % (callback, now))
    callback()
    now = time.time() - now
    print('%s - spent: %f Second' % (callback, now))


def timestamp_to_time(timestamp):
    x = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', x)


def time_to_timestamp(time_str):
    x = time.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    return time.mktime(x)


def get_current_timestamp():
    return time.time()

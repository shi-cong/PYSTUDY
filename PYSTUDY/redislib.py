"""
redis模块封装
"""
import redis


class RedisPool(object):
    """redis连接池封装"""

    def __init__(self, host, port):
        """创建连接"""
        pool = redis.ConnectionPool(host=host, port=port)
        self.client = redis.Redis(connection_pool=pool)

    def set(self, name, value, ex=None, px=None, nx=False, xx=False):
        """设置值，不存在则创建，存在则修改
        :param name: key
        :param value: value
        :param ex: 过期时间（秒）
        :param px: 过期时间（毫秒）
        :param nx: 如果设置为True，则只有name不存在时，当前的set操作才执行
        :param xx: 如果设置为True，则只有nmae存在时，当前的set操作才执行
        """
        self.client.set(name=name, value=value, px=px, nx=nx, xx=xx)

    def get(self, name):
        """获取某以key的值
        :param name: key
        :return: 返回获取的值
        """
        return self.client.get(name)

    def incr(self, name, amount=1):
        """自增key的对应的值，当key不存在时则为默认值，否则在基础上自增整数amount
        :param name: key
        :param amount: 默认值
        :return: 返回自增后的值
        """
        return self.client.incr(name, amount=amount)
        
    def decr(self, name, amount=1):
        """递减key的对应的值，当key不存在时则为默认值，否则在基础上递减整数amount
        :param name: key
        :param amount: 默认值
        :return: 返回递减后的值
        """
        return self.client.decr(name, amount=amount)

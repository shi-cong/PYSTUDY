"""
mysql模块
"""
from functools import partial
import traceback
from threading import Lock, current_thread

import pymysql
import tormysql

from tornado.ioloop import IOLoop
from tornado import gen


class _MySQLConnection(dict):
    is_used = None
    connection = None


class MYSQLPool(object):
    """
    mysql连接池类
    需要注意的是，每条sql语句的第一个字符不能是空格
    当连接池中没有可用的连接时，将创建新的mysql连接
    """
    def __init__(self, size, **kwargs):
        self._pool = []
        self.lock = Lock()
        self.kwargs = kwargs
        kwargs['cursorclass'] = pymysql.cursors.DictCursor
        for i in range(size):
            self._pool.append(
                _MySQLConnection(
                    is_used=False, connection=pymysql.Connection(**kwargs)))

    def close(self):
        for i in self._pool:
            i['connection'].close()

    def _get_connection(self):
        with self.lock:
            while 1:
                for conn in self._pool:
                    if not conn['is_used']:
                        conn['is_used'] = True
                        return conn
                    else:
                        continue

                if len(self._pool) == 100:
                    continue
                else:
                    newConn = _MySQLConnection(
                            is_used=False, connection=pymysql.Connection(**kwargs))
                    self._pool.append(newConn)
                    return newConn

    def execute(self, sql, args=None):
        conn = self._get_connection()
        tmp = ''
        try:
            with conn['connection'].cursor() as cursor:
                cursor.execute(sql, args or ())
                tmp = sql[:6].lower()
                if 'insert' in tmp or 'delete' in tmp or 'update' in tmp:
                    conn['connection'].commit()
                if 'select' in tmp:
                    rows = cursor.fetchall()
                    result = []
                    for row in rows:
                        result.append(row)
                    return result
                else:
                    affected = cursor.rowcount
                    return affected
        except:
            err = traceback.format_exc()
            print(err)
            if 'insert' in tmp or 'delete' in tmp or 'update' in tmp:
                conn['connection'].rollback()
            if 'MySQL Connection not available' in err:
                conn['connection'] = _MySQLConnection(
                    is_used=False, connection=pymysql.Connection(**self.kwargs))
        finally:
            cursor.close()
            conn['is_used'] = False


class AsyncMySQLPool(object):
    """异步mysql连接池"""

    def __init__(self, host, user, passwd, db, charset='utf8', 
            max_connections=20, idle_seconds=7200, wait_connection_timeout=3):
        """初始化连接池
        :param host: 主机地址
        :param user: 用户名
        :param passwd: 密码
        :param db: 数据库名
        :param charset: 编码
        :param max_connections: 最大连接数
        :param idle_seconds: 
        :param wait_connection_timeout:
        """
        self._pool = tormysql.ConnectionPool(
            max_connections=max_connections,
            idle_seconds=idle_seconds,
            wait_connection_timeout=wait_connection_timeout,
            host=host, user=user, passwd=passwd, db=db, charset=charset)
        self.ioloop = IOLoop.instance()

    def close(self):
        self._pool.close()

    def execute(self, sql):
        func = partial(self._execute, sql=sql)
        return self.ioloop.run_sync(func)

    @gen.coroutine
    def _execute(self, sql):
        """执行sql语句
        :param sql: sql语句
        :return: 返回的都是数组对象
        """
        sql = sql.lower().strip()
        tmp = sql[:6]
        with (yield self._pool.Connection()) as conn:
            try:
                with conn.cursor() as cursor:
                    yield cursor.execute(sql)
                    if tmp == 'select':
                        datas = cursor.fetchall()   
                        return datas
            except Exception as e:
                if tmp in ['insert', 'update']:
                    yield conn.rollback()
                raise e
            else:
                if tmp in ['insert', 'update']:
                    yield conn.commit()

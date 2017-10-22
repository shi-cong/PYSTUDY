"""
mysql模块
"""
import logging
import traceback
from threading import Lock, current_thread

import pymysql


class _MySQLConnection(dict):
    is_used = None
    connection = None


class MYSQLPool(object):
    """
    mysql连接池类
    需要注意的是，每条sql语句的第一个字符不能是空格
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

                logging.debug(('%r - waitting for other thread to release the'
                               'connection' % current_thread()))

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

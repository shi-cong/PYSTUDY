"""异步mysql测试"""
import import_module
from PYSTUDY.unittestlib import TestCase, run_one_test
from PYSTUDY.middleware.mysqllib import AsyncMySQLPool, MYSQLPool, get_mysql_pool


class MySQLLIBTest(TestCase):
    def test_async(self):
        host = '192.168.80.4'
        user = 'root'
        passwd = 'xx'
        db = 'xx'
        sql = 'select * from video where catId=%s limit 10'
        args = (319,)
        amsp = AsyncMySQLPool(host, user, passwd, db, size=20)
        datas = amsp.execute(sql, args)
        print(datas)
        amsp.close()

    def test_async_kwargs(self):
        kwargs = {
            'user': 'root',
            'host': '192.168.80.4',
            'password': 'xx',
            'db': 'xx',
            'size': 20,
        }
        sql = 'select * from xx where catId=319 limit 10'
        amsp = AsyncMySQLPool(**kwargs)
        datas = amsp.execute(sql)
        print(datas)
        amsp.close()

    def test_kwargs(self):
        kwargs = {
            'user': 'root',
            'host': '192.168.80.4',
            'password': 'xx',
            'db': 'xx',
            'size': 20,
        }
        sql = 'select * from xx where catId=319 limit 10'
        amsp = MYSQLPool(**kwargs)
        datas = amsp.execute(sql)
        print(datas)
        amsp.close()

    def test_factory_method(self):
        kwargs = {
            'user': 'root',
            'host': '192.168.80.4',
            'password': 'xx',
            'db': 'xx',
            'size': 20,
            'isSync': True,
        }
        sql = 'select * from xx where catId=319 limit 10'
        mp = get_mysql_pool(**kwargs)
        datas = mp.execute(sql)
        print(datas)
        mp.close()

    def test_insert_id(self):
        kwargs = {
            'user': 'root',
            'host': '192.168.80.4',
            'password': 'xx',
            'db': 'xx',
            'size': 20,
            'isSync': False,
        }
        sql = ('insert into category(name, url, totalPages, updatedTime, responseTime)'
               ' values("test", "www.test.com", 1, 0, 0)')
        mp = get_mysql_pool(**kwargs)
        insertId = mp.execute(sql)
        print(insertId)
        mp.close()


if __name__ == '__main__':
    run_one_test(MySQLLIBTest, 'test_async')
    # run_one_test(MySQLLIBTest, 'test_async_kwargs')
    # run_one_test(MySQLLIBTest, 'test_kwargs')
    # run_one_test(MySQLLIBTest, 'test_factory_method')
    # run_one_test(MySQLLIBTest, 'test_insert_id')

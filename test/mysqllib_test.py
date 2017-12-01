"""异步mysql测试"""
import import_module
from PYSTUDY.unittestlib import TestCase, run_one_test
from PYSTUDY.middleware.mysqllib import AsyncMySQLPool


class MySQLLIBTest(TestCase):
    def test_async(self):
        host = '192.168.80.4'
        user = 'xxx'
        passwd = 'xxx'
        db = 'xxx'
        sql = 'select * from xxx where catId=319 limit 10'
        amsp = AsyncMySQLPool(host, user, passwd, db)
        datas = amsp.execute(sql)
        print(datas)
        amsp.close()

if __name__ == '__main__':
    run_one_test(MySQLLIBTest, 'test_async')

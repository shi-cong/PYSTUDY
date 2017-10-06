from shicong.mysqllib import MYSQLPool
from shicong.yamllib import Yaml

mysql_pool = MYSQLPool(20,
                    **Yaml('db.yaml').get('ss'))

def get(keyword, page=1):
    keyword = '%keyword%'
    sql = "select * from kws where keyword like %s order by update_time desc limit " + str((page-1)*10) + "," + str(page*10)
    return mysql_pool.execute(sql, keyword)


if __name__ == '__main__':
    print(get('python'))
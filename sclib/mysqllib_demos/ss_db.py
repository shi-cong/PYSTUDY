from sclib.mysqllib import MYSQLPool

mysql_pool = MYSQLPool(20,
                    **dict(host='192.168.80.4',
                           user='ss',
                           password='123456',
                           db='ss',
                           charset='utf8mb4'))

def get(keyword, page=1):
    keyword = '%keyword%'
    sql = "select * from kws where keyword like %s order by update_time desc limit " + str((page-1)*10) + "," + str(page*10)
    return mysql_pool.execute(sql, keyword)


if __name__ == '__main__':
    print(get('python'))
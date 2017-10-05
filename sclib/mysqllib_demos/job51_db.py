from sclib.mysqllib import MYSQLPool

mysql_pool = MYSQLPool(20,
                    **dict(host='192.168.80.4',
                           user='job51',
                           password='123456',
                           db='job51',
                           charset='utf8mb4'))

def add_my_apply(*params):
    if len(params) != 7:
        raise Exception('参数不对')
    sql = 'insert into my_apply(job_name, pay, job_url, submit_time, submit_nums, company_name, company_url) ' \
          'values(%s, %s, %s, %s, %s, %s, %s)'
    mysql_pool.execute(sql, params)

def add_job(*params):
    sql = 'insert into job(job_id, job_name, company, addr, money, pub_time) ' \
          'values(%s, %s, %s, %s, %s, %s)'
    mysql_pool.execute(sql, params)
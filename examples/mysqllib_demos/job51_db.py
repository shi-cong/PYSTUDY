from shicong.mysqllib import MYSQLPool
from shicong.yamllib import Yaml


mysql_pool = MYSQLPool(20,
                    **Yaml('../db.yaml').get('job51'))

def add_my_apply(*params):
    """
    增加我的投递
    :param params:
    :return:
    """
    if len(params) != 7:
        raise Exception('参数不对')
    sql = 'insert into my_apply(job_name, pay, job_url, submit_time, submit_nums, company_name, company_url) ' \
          'values(%s, %s, %s, %s, %s, %s, %s)'
    mysql_pool.execute(sql, params)

def add_job(*params):
    """

    :param params:
    :return:
    """
    sql = 'insert into job(job_id, job_name, company, addr, money, pub_time) ' \
          'values(%s, %s, %s, %s, %s, %s)'
    mysql_pool.execute(sql, params)
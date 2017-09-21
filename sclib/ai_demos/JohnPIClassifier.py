# -*- coding: utf-8 -*-
'''
这个程序描述了这样一件故事，Johny喜欢吃一个叫做派的东西，然后这个派有这么
几种属性，

外壳形状(shape-, circle[圆], triangle[三角形], square[矩形]),
外壳大小(crust-size-, thick[厚], thin[薄]),
外壳色度(crust-shade-, dark[黑], white[白], gray[灰]),
内馅大小(filling-size-, thick[厚], thin[薄]),
内馅色度(filling-shade-, dark[黑], white[白], gray[灰]),

然后，根据我随机生成的样本, 来预测当Johny说一个外壳形状时的那个派是Johny喜欢
的，还是他不喜欢的，喜欢的定义为pos,不喜欢的定义为neg,根据贝叶斯公式，
当输入shape 为 circle时，P(shape=circle, cat=pos) | P(shape=circle) 即可计算出
，在所有的外壳形状为圆形，为正类的条件概率分布。
同理，可以计算出在所有的外壳形状为圆形时，为负类的条件概率分布。
由于pos > neg 则可以判断，当输入shape=circle时，为Johny喜欢的派,
否则就是Johny不喜欢的派。
'''
import sqlite3
import random
import time
import sys

XRANGE = range
if sys.platform.startswith('2.7'):
    XRANGE = xrange


class Sample(object):
    ''''''
    def __init__(self, shape, crust_size, crust_shade, filling_size,
                 filling_shade, category):
        self.shape = shape
        self.crust_size = crust_size
        self.crust_shade = crust_shade
        self.filling_size = filling_size
        self.filling_shade = filling_shade
        self.category = category


def init_db():
    conn = sqlite3.connect('1.1.db')
    c = conn.cursor()
    try:
        tb_name = '1_1'
        sql = '''
            create table tb_%s(
            id int primary key,
            shape text,
            crust_size text,
            crust_shade text,
            filling_size text,
            filling_shade text,
            category text)
            ''' % tb_name
        print(sql)
        c.execute(sql)
    except:
        pass
    finally:
        c.close()
        conn.close()


def insert_ex(tb_name, sample):
    conn = sqlite3.connect('1.1.db')
    c = conn.cursor()
    args = (
        tb_name,
        sample.shape,
        sample.crust_size,
        sample.crust_shade,
        sample.filling_size,
        sample.filling_shade,
        sample.category, )
    sql = ("insert into %s(shape, crust_size, crust_shade, filling_size,"
           "filling_shade, category) values('%s','%s','%s','%s','%s','%s')")
    sql = sql % args
    print(sql)
    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()


def select_shape(tb_name, shape_ex):
    '''外壳形状的预测函数
    '''
    # pudb.set_trace()
    conn = sqlite3.connect('1.1.db')
    c = conn.cursor()
    pos_shape = ("select count(*) as pos_shape from %s where shape='%s' and "
                 "category='pos'" % (tb_name, shape_ex))
    c.execute(pos_shape)
    result = c.fetchone()
    pos_shape = float(result[0])

    shape = ("select count(*) as shape from %s where shape='%s'" % (tb_name,
                                                                    shape_ex))
    c.execute(shape)
    result = c.fetchone()
    shape = float(result[0])

    # 1
    pos_shape__shape = pos_shape / shape
    print('input: shape=%s' % shape_ex)
    print('P(pos * shape=%s) / P(shape=%s) = %f' % (pos_shape, shape,
                                                    pos_shape__shape))

    neg_shape = ("select count(*) as neg_shape from %s where shape='%s' and"
                 " category='neg'" % (tb_name, shape_ex))
    c.execute(neg_shape)
    result = c.fetchone()
    neg_shape = float(result[0])

    # 2
    neg_shape__shape = neg_shape / shape
    print('P(neg * shape=%s) / P(shape=%s) = %f' % (neg_shape, shape,
                                                    neg_shape__shape))

    c.close()
    conn.close()
    print('output:')
    if pos_shape__shape > neg_shape__shape:
        return 'pos'
    else:
        return 'neg'


def select_crust_size(tb_name, crust_size_ex):
    '''外壳大小的预测函数
    '''
    # pudb.set_trace()
    conn = sqlite3.connect('1.1.db')
    c = conn.cursor()
    pos_crust_size = (
        "select count(*) as pos_crust_size from %s where crust_size='%s' and "
        "category='pos'" % (tb_name, crust_size_ex))
    c.execute(pos_crust_size)
    result = c.fetchone()
    pos_crust_size = float(result[0])

    crust_size = ("select count(*) as crust_size from %s where crust_size='%s'"
                  % (tb_name, crust_size_ex))
    c.execute(crust_size)
    result = c.fetchone()
    crust_size = float(result[0])

    # 1
    # 条件概率P(pos|crust_size)
    pos_crust_size__crust_size = pos_crust_size / crust_size
    print('input: crust_size=%s' % crust_size_ex)
    print('P(pos * crust_size=%s) / P(crust_size=%s) = %f' %
          (pos_crust_size, crust_size, pos_crust_size__crust_size))

    neg_crust_size = (
        "select count(*) as neg_crust_size from %s where crust_size='%s' and"
        " category='neg'" % (tb_name, crust_size_ex))
    c.execute(neg_crust_size)
    result = c.fetchone()
    neg_crust_size = float(result[0])

    # 2
    neg_crust_size__crust_size = neg_crust_size / crust_size
    print('P(neg * crust_size=%s) / P(crust_size=%s) = %f' %
          (neg_crust_size, crust_size, neg_crust_size__crust_size))

    c.close()
    conn.close()
    print('output:')
    if pos_crust_size__crust_size > neg_crust_size__crust_size:
        return 'pos'
    else:
        return 'neg'


def select_crust_shade(tb_name, crust_shade_ex):
    '''外壳色度的预测函数
    '''
    conn = sqlite3.connect('1.1.db')
    c = conn.cursor()
    # 查询外壳色度为正类的个数
    pos_crust_shade = (
        "select count(*) as pos_crust_shade from %s where crust_shade='%s' and "
        "category='pos'" % (tb_name, crust_shade_ex))
    c.execute(pos_crust_shade)
    result = c.fetchone()
    pos_crust_shade = float(result[0])

    # 查询外壳色度的个数
    crust_shade = ("select count(*) as crust_shade from %s where crust_shade='%s'"
                  % (tb_name, crust_shade_ex))
    c.execute(crust_shade)
    result = c.fetchone()
    crust_shade = float(result[0])

    # 1
    # 条件概率P(pos|crust_size)
    pos_crust_shade__crust_shade = pos_crust_shade / crust_shade
    print('input: crust_shade=%s' % crust_shade_ex)
    print('P(pos * crust_shade=%s) / P(crust_shade=%s) = %f' %
          (pos_crust_shade, crust_shade, pos_crust_shade__crust_shade))

    # 查询外壳色度为负类的个数
    neg_crust_shade = (
        "select count(*) as neg_crust_shade from %s where crust_shade='%s' and"
        " category='neg'" % (tb_name, crust_shade_ex))
    c.execute(neg_crust_shade)
    result = c.fetchone()
    neg_crust_shade = float(result[0])

    # 2
    neg_crust_shade__crust_shade = neg_crust_shade / crust_shade
    print('P(neg * crust_shade=%s) / P(crust_shade=%s) = %f' %
          (neg_crust_shade, crust_shade, neg_crust_shade__crust_shade))

    c.close()
    conn.close()
    print('output:')
    if pos_crust_shade__crust_shade > neg_crust_shade__crust_shade:
        return 'pos'
    else:
        return 'neg'

def generate_train_data():
    init_db()
    for j in XRANGE(1):
        for i in XRANGE(random.randint(10, 100)):
            shape = random.sample(['circle', 'triangle', 'square'], 1)[0]
            crust_size = random.sample(['thick', 'thin'], 1)[0]
            crust_shade = random.sample(['gray', 'white', 'dark'], 1)[0]
            filling_size = random.sample(['thick', 'thin'], 1)[0]
            filling_shade = random.sample(['white', 'gray', 'dark'], 1)[0]
            category = random.sample(['pos', 'neg'], 1)[0]

            sample = Sample(shape, crust_size, crust_shade, filling_size,
                            filling_shade, category)
            insert_ex(tb_name, sample)
        time.sleep(1)


if __name__ == '__main__':
    tb_name = 'tb_1_1'
    generate_train_data()
    print(select_shape(tb_name, 'circle'))
    print(select_crust_size(tb_name, 'thick'))
    print(select_crust_shade(tb_name, 'gray'))
    import os
    os.remove('1.1.db')
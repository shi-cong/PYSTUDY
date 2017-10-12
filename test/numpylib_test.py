from unittest import TestCase
from shicong.numpylib import tile, arange, array, array_len, eye, savetxt, loadtxt, vwap, mean, twap, weight, median
import shicong.numpylib as nplb

class NumpylibTestCase(TestCase):
    def test_1(self):
        """向量加法"""
        a = arange(10) ** 2
        b = arange(10, dtype=int) ** 3
        c = arange(1, 20, 2, float)

        d = a + b + c
        print(a, b, c)
        print(d)

    def test_work_1_1(self):
        w1 = arange(1,6)
        print(w1)

        w2 = arange(5)
        print(w2)

    def test_2(self):
        m = array([arange(2), arange(2)])
        print(m)

        print(array_len(m))

    def test_work_2_1(self):
        m = array([arange(3), arange(1,4), arange(2,5)])

        print(m)
        print(m[0, 0])
        print(m[0, 1])

    def test_3_1(self):
        i2 = eye(2, dtype=nplb.int)
        print(i2)
        savetxt("numpylib_data/eye.txt", i2)

    def test_3_2(self):
        """计算加权平均数"""
        c, v = loadtxt('numpylib_data/abcdefg.csv', dtype=nplb.float, delimiter=',', usecols=(5,6), unpack=True)
        vp =  vwap(c, weights=v)
        print(c, v, vp)

        print(mean(c))

        print(twap(c, weights=weight(c)))

        print(nplb.max(c), nplb.min(c))

        print(nplb.median(c))

        print(nplb.var(c))


    def test_write_csv_big_data(self):
        """
        通过这次单元测试，得出了一个结论，numpy如果用来加载大容量的csv，时间会非常慢，
        这个测试在我的mac上跑了有14个小时。所以，如果在遇到这种比较大的数据时，要慎用
        这个loadtxt的函数。s
        :return:
        """
        # out = '1,2,3,4,5,6,7'
        filename = 'numpylib_data/bigdata.csv'
        # f = open(filename, 'w')
        # for i in range(10**10):
        #     f.write(out + '\n')
        # f.flush()
        # f.close()

        # print("写入数据完成")

        c = loadtxt(filename, delimiter=',')
        print(c)

        print('读取数据成功')
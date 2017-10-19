##
# @file numpylib.py
# @brief
# @author shi-cong
# @version
# @date 2017-10-14

"""
numpy模块
"""
import numpy

########################################################################################################################
#               数                       据                      类                     型
########################################################################################################################
bool = numpy.bool  # 值为 True 或 False

# 有符号整数
int8 = numpy.int8
int16 = numpy.int16
int32 = numpy.int32
int64 = numpy.int64
# int128 = numpy.int128
int = numpy.int

# 无符号整数
uint8 = numpy.uint8
uint16 = numpy.uint16
uint32 = numpy.uint32
uint64 = numpy.uint64
# uint128 = numpy.uint128

# 有符号浮点数
float16 = numpy.float16
float32 = numpy.float32
float64 = numpy.float64
# float80 = numpy.float80
# float96 = numpy.float96
float128 = numpy.float128
# float256 = numpy.float256
float = numpy.float

# 复数
# complex32 = numpy.complex32
complex64 = numpy.complex64
complex128 = numpy.complex128
# complex160 = numpy.complex160
# complex192 = numpy.complex192
complex256 = numpy.complex256
# complex512 = numpy.complex512

# 字符串
string = numpy.str  #

"""
有相应的类型转换函数
>>> flaot64(42)
42.0
>>> int8(42.0)
42
>>> bool(42)
True
>>> float(True)
1.0
>>> float(False)
0.0
"""

dtype = numpy.dtype
"""
dtype用于创建自定义数据类型
"""


########################################################################################################################
#               创                                                       建
########################################################################################################################
"""
相关参数：
1. shape 可以是int类型数据，或者是int类型的序列。表示新的数组的大小
2. dtype 数组数据类型，默认为float
3. order 在内存中排列的方式（以C语言或Fortran语言方式排列），默认为C语言排列
"""

array = numpy.array

arange = numpy.arange
"""
arange函数用于创建等差数组，使用频率非常高，arange非常类似range函数，
会python的人肯定经常用range函数，比如在for循环中，几乎都用到了range，
下面我们通过range来学习一下arange，两者的区别仅仅是arange返回的是一
个数据，而range返回的是list。
"""

ndarray = numpy.ndarray
"""
这个用的不多，array可以取代他
"""

zeros = numpy.zeros
"""
创建给定类型的矩阵，并初始化为0
"""


zeros_like = numpy.zeros_like
"""
返回和输入大小相同，类型相同，用0填满的数组
"""


ones_like = numpy.ones_like
"""
返回和输入大小相同，数据类型相同，用1填满的数组
"""


empty_like = numpy.empty_like
"""
返回和输入大小相同，数据类型相同，但是是未初始化的数组(数据随机)
"""


ones = numpy.ones
"""
返回一个和输入大小相同，数据类型相同，初始化为1的数组
"""

empty = numpy.empty
"""
返回一个新的未初始化的数组
"""

tile = numpy.tile
"""
numpy.tile()是个什么函数呢，说白了，就是把数组沿各个方向复制
比如 a = np.array([1,2]),
np.tile(a,(2,1))就是把a先沿x轴（就这样称呼吧）复制1倍，即没有复制，仍然是 [1,2]。
再把结果沿y方向复制2倍，即最终得到
 array([[1,2],
        [1,2]])
同理：
>>> b = np.array([[1, 2], [3, 4]])
>>> np.tile(b, 2) #沿X轴复制2倍
array([[1, 2, 1, 2],
       [3, 4, 3, 4]])
>>> np.tile(b, (2, 1)) #沿X轴复制1倍（相当于没有复制），再沿Y轴复制2倍
array([[1, 2],
       [3, 4],
       [1, 2],
       [3, 4]])
"""

eye = numpy.eye
"""
创建单位矩阵，对角线上的元素均为1
"""

########################################################################################################################
#               排                                                                       序
########################################################################################################################
def argsort(arr):
    """对数组进行排序, 返回以索引的数组"""
    return arr.argsort()


########################################################################################################################
#               运                                                                       算
########################################################################################################################
def exponential_operation(arr, expo):
    """矩阵指数运算"""
    return arr ** expo

def array_sum(arr, axis=1):
    """矩阵内元素求和"""
    return arr.sum(axis=1)

vwap = numpy.average
"""
加权平均是统计学的一个概念，一组数据中某一个数的频数称为权重，简单说就是，数值乘以频数再除以总数据个数 就是加权平均了。
加权平均就是，每个数乘以自己所占的份额（%），然后加起来的和。
比如：一种物品，它有A、B、C、D四种报价，各自的份额为20%，15%，30%，35%则加权平均数（价）就是（A*20+B*15+C*30+D*35）/100
黄金报价：
有最高价和最低价2种，其中最高价261.79，占57.3%；最低价255，占42.7%。
那黄金的加权平均价为：261.79*57.3%+255*42.7%=258.89

另外：
成交量加权平均价格(vwap)是一个非常重要的经济学量，它代表着金融资产的"平均"价格。某个价格的成交量越高，该价格所占的权重就越大,
权重越大，该金融产品的市场的占用率就越大(个人觉得)。
vwap就是以成交量为权重计算出来的加权平均值，常用语算法交易。

"""

def weight(c):
    """求权重"""
    return arange(len(c))

def twap(c, weights):
    """
    时间加权平均价格(twap)是另一种"平均"价格的指标，是一种变种的成交量平均价格(vwap)，基本思想就是最近的价格重要性大一些，所以我们
    应该对近期的价格给以较高的权重。
    """
    return vwap(c, weights=weights)

mean = numpy.mean
"""
算数平均值函数
"""

max = numpy.max
min = numpy.min

"""
中位数：作用（去除异常值）通常就是用这个值来
将各个变量值按大小顺序排列起来，形成一个数列，局域数列中间位置的那个数即为中位数。
"""
def median(c):
    """
    计算中位数
    :param c: 数组
    :return:
    """
    return numpy.median(c)

"""
方差:
方差能体现变量变化的程度，在某些场景，方差可以告诉我们风险投资的大小。方差越小，投资风险越小.

方差是指各个数据与所有数据算数平局数的离差平方和除以数据个数所得到的值。
"""
def var(c):
    """计算方差"""
    return numpy.var(c)

########################################################################################################################
#               属                                                                       性
########################################################################################################################
def array_len(arr):
    """矩阵长度"""
    return arr.shape[0]

def get_array_dtype(arr):
    """数组数据类型"""
    return arr.dtype

def get_array_one_itemsize(arr):
    """计算单个数组元素在内存中占用的字节数"""
    return get_array_dtype(arr).itemsize

def get_array_all_itemsize(arr):
    # 获取数组占的内存大小
    return arr.nbytes

########################################################################################################################
#               组               合               操               作
########################################################################################################################
def ravel(arr, new_memory=False):
    """将数组展平"""
    return arr.ravel() if not new_memory else arr.flatten()

def transpose(arr):
    """线性代数中的转置矩阵"""
    return arr.transpose()

def reseize(arr, *param):
    """改变数组纬度"""
    arr.resize(param)

def hstack(*params):
    # 水平数组组合
    # 水平组合就是将多个数组以每一行的所有元素放到一个新的数组里组成一个数组保存到矩阵中
    # 对于2纬数组 就是column_stack列组合
    return numpy.hstack(params)

def vstack(*params):
    # 垂直数组组合
    # 对于二纬数组 列组合
    return numpy.vstack(params)

def dstack(*params):
    # 深度组合
    return numpy.dstack(params)

def equals(arr1, arr2):
    """计算两个数组中的每一个元素是否相等"""
    return arr1 == arr2

########################################################################################################################
#               分               割               操               作
########################################################################################################################
def hsplit(arr):
    """水平分割"""
    return numpy.hsplit(arr, array_len(arr))

def vsplit(arr):
    """垂直分割"""
    return numpy.vsplit(arr, array_len(arr))

def dsplit(arr):
    """按深度方向进行分割"""
    return numpy.dsplit(arr, array_len(arr))

########################################################################################################################
#               转                                                   换
########################################################################################################################
def to_list(arr):
    """转换为列表"""
    return arr.tolist()

########################################################################################################################
#               持                                   久                                       化
########################################################################################################################
def savetxt(filename, arr):
    numpy.savetxt(filename, arr)

# 加载数据
loadtxt = numpy.loadtxt # 加载csv文件
"""
c, v = loadtxt('data.csv', delimiter=',', usecols=(6,7), unpack=True)

>>> c = StringIO("1,0,2\\n3,0,4")
    >>> x, y = np.loadtxt(c, delimiter=',', usecols=(0, 2), unpack=True)
    >>> x
    array([ 1.,  3.])
    >>> y
    array([ 2.,  4.])
"""

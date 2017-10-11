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
int128 = numpy.int128
int = numpy.int

# 无符号整数
uint8 = numpy.uint8
uint16 = numpy.uint16
uint32 = numpy.uint32
uint64 = numpy.uint64
uint128 = numpy.uint128

# 有符号浮点数
float16 = numpy.float16
float32 = numpy.float32
float64 = numpy.float64
float80 = numpy.float80
float96 = numpy.float96
float128 = numpy.float128
float256 = numpy.float256
float = numpy.float

# 复数
complex32 = numpy.complex32
complex64 = numpy.complex64
complex128 = numpy.complex128
complex160 = numpy.complex160
complex192 = numpy.complex192
complex256 = numpy.complex256
complex512 = numpy.complex512

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
#               矩                       阵                      操                     作                                                                                                       ##
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
# 排序
def argsort(arr):
    """对数组进行排序, 返回以索引的数组"""
    return arr.argsort()

# 运算
def exponential_operation(arr, expo):
    """矩阵指数运算"""
    return arr ** expo

def array_sum(arr, axis=1):
    """矩阵内元素求和"""
    return arr.sum(axis=1)

# 属性
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

# 组合操作
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

# 分割操作
def hsplit(arr):
    """水平分割"""
    return numpy.hsplit(arr, array_len(arr))

def vsplit(arr):
    """垂直分割"""
    return numpy.vsplit(arr, array_len(arr))

def dsplit(arr):
    """按深度方向进行分割"""
    return numpy.dsplit(arr, array_len(arr))

# 转换
def to_list(arr):
    """转换为列表"""
    return arr.tolist()
"""
numpy模块
"""
import numpy


#################################################################################################################################
#               矩                       阵                      操                     作                                                                                                       ##
#################################################################################################################################
"""
相关参数：
1. shape 可以是int类型数据，或者是int类型的序列。表示新的数组的大小
2. dtype 数组数据类型，默认为float
3. order 在内存中排列的方式（以C语言或Fortran语言方式排列），默认为C语言排列
"""

array = numpy.array

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

def argsort(arr):
    """
    对数组进行排序, 返回以索引的数组
    """
    return arr.argsort()

def exponential_operation(arr, expo):
    """
    矩阵指数运算
    """
    return arr ** expo

def array_sum(arr, axis=1):
    """矩阵内元素求和"""
    return arr.sum(axis=1)

def array_len(arr):
    """矩阵长度"""
    return arr.shape[0]

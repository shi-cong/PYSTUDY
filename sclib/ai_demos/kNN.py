'''
k近邻算法实现

优点：精度高，对异常值不敏感，无数据输入假定
缺点：时间复杂度高，空间复杂度高
适用数据范围：数值型和标称型

标称型：标称型目标变量的结果只在有限目标集中取值，如真与假(标称型目标变量主要用于分类)
数值型：数值型目标变量则可以从无限的数值集合中取值，如0.100，42.001等 (数值型目标变量主要用于回归分析)

这个算法经过我的研究：
1. 有局限性，主要体现在这几个方面
    * k的值只能最大不能大于训练样本集的大小，最小不能小于1
    * k会影响分类的精确度, 比如，如果这个例子，我给k设置为4， 这里就会出现最相似数据中出现次数都为2，这样你就无法判断哪个分类作为新数据的分类了。
    * 总体来说，精确度与A的值是有关系的。其实，我觉得这个算法还是相对的。

最后，我的疑惑可以用百度百科来解释。我90%的理解很赞同百度百科的解释。
https://baike.baidu.com/item/k%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95/9512781?fr=aladdin
'''
from sclib.numpylib import *

import operator


def create_data_set():
    """
    导入数据
    :return:
    """
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(in_x, data_set, labels, k):
    """
    kNN分类算法
    :param in_x: 用于分类的输入向量
    :param data_set: 输入训练样本集
    :param labels: 类别标签向量
    :param k: 用于选择最近邻居的数目
    :return: 返回k个最相似数据中出现次数最多的分类
    """
    # data_set_size = data_set.shape[0]
    data_set_size = len(data_set)
    # 距离计算
    diff_mat = tile(in_x, (data_set_size, 1)) - data_set  # 计算
    sq_diff_mat = diff_mat ** 2  # 求数组的平方
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances ** 0.5

    sorted_dist_indicies = distances.argsort()  # 数组值从小到大的索引值

    class_count = {}

    # 选择距离最小的k个点
    for i in range(k):
        vote_i_label = labels[sorted_dist_indicies[i]]
        class_count[vote_i_label] = class_count.get(vote_i_label, 0) + 1

    # 排序
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count


def main():
    group, labels = create_data_set()
    sorted_class_count = classify0([0, 0], group, labels, 5)
    print(sorted_class_count)


main()

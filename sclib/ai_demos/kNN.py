'''
k近邻算法实现

优点：精度高，对异常值不敏感，无数据输入假定
缺点：时间复杂度高，空间复杂度高
适用数据范围：数值型和标称型

标称型：标称型目标变量的结果只在有限目标集中取值，如真与假(标称型目标变量主要用于分类)
数值型：数值型目标变量则可以从无限的数值集合中取值，如0.100，42.001等 (数值型目标变量主要用于回归分析)
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
    diff_mat = tile(in_x, (data_set_size, 1)) - data_set # 计算
    sq_diff_mat = diff_mat ** 2 # 求数组的平方
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances ** 0.5

    sorted_dist_indicies = distances.argsort() # 数组值从小到大的索引值

    class_count = {}

    # 选择距离最小的k个点
    for i in range(k):
        vote_i_label = labels[sorted_dist_indicies[i]]
        class_count[vote_i_label] = class_count.get(vote_i_label, 0) + 1

    # 排序
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


def main():
    group, labels = create_data_set()
    sorted_class_count = classify0([-1, -1], group, labels, 3)
    print(sorted_class_count)


main()
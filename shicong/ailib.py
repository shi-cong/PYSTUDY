"""
ai模块
"""


class BaseData:
    """
    数据基类
    """

    def __init__(self, attributes=dict(), category_label=None):
        """
        创建一个数据样例对象
        :param attributes:  k: v  k属性名称， v属性的数字化表示
        :param category_label: 类别标签，有类别则不为None
        """
        self.attributes = attributes
        self.category_label = category_label


class MSIB:
    """
    贝叶斯分类模型
    """

    def classification(self, func, example):
        """
        分类算法
        :param func: 进行分类的回调函数
        :param params: 其它分类需要的参数
        :return: 算出的分类
        """
        category = func(example)
        return category

    def train(self, examples):
        """
        训练得到最佳参数
        :param examples: 训练样例
        :return: 返回参数的区间范围
        """
        pass


class KNN:
    """
    kNN近邻分类模型
    """

    def train(self, func, *params):
        func(*params)

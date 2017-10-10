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

DataExample = BaseData # 数据样例

TrainExample = BaseData # 训练样例


class MSIB:
    """
    贝叶斯分类模型
    """

    def classification(self, left_neighborhod, right_neighborhod, func, *params):
        """
        分类算法
        :param left_neighborhod: 左邻域
        :param right_neighborhod: 右邻域
        :param func: 进行分类的回调函数
        :param params: 其它分类需要的参数
        :return: 算出的分类
        """
        category = func(*params)
        return category

    def train(self, left_neighborhood, right_neighborhod, examples):
        """
        训练left_neghborhod和right_neighborhod的值以达到预测的最佳效果
        :param left_neighborhood: 左邻域
        :param right_neighborhod: 右邻域
        :param examples: 测试样例
        :return: 返回预测的正确率
        """
        # 总共训练数据的个数
        tte = len(examples)
        right = 0 # 正确分类的个数

        for example in examples:
            category = self.classification(left_neighborhood, right_neighborhod, example)
            if category == example.category:
                right += 1
        return right / tte


class KNN:
    """
    kNN近邻分类模型
    """
    def train(self, func, *params):
        func(*params)
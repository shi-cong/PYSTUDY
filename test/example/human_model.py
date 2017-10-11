"""
贝叶斯分类模型例子
"""
from shicong.ailib import BaseData, MSIB
from shicong.randomlib import random_int, random_set, random_float

Human = BaseData

def human_classification(train_example):
    passn

def genearte_human_data_set(size):
    """
    随机生成human数据集
    :param size: 大小
    :return:
    """
    data_examples = []
    for i in range(size):
        people = Human()
        people.attributes['头发长度'] = random_int(0, 50)    # 随机头发的长度
        people.attributes['身高'] = random_float(50, 240)     # 随机身高
        people.attributes['胸围'] = random_set(1, ['None', 'A', 'B', 'C', 'D'])  # 随机胸围
        people.category_label = random_set(1, ['男', '女']) # 随机性别
        data_examples.append(people)
    return data_examples

def train_human_model():
    # 收集数据
    train_examples = genearte_human_data_set(1000)  # 训练集
    test_examples = genearte_human_data_set(10)  # 测试集
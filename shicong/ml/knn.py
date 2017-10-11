"""
knn近邻算法的简单编写
"""
from shicong.numpylib import array, tile, argsort, array_sum, array_len, exponential_operation
from shicong.coolectionslib import odict

def load_data():
    groups = array([[1, 1, 1, 1],
                    [2, 2, 2, 2],
                    [3, 3, 3, 3],
                    [4, 4, 4, 4]])
    lables = ['A', 'B', 'B', 'C']

    return groups, lables


def classify(in_x, groups, labels, k):
    """分类"""
    # 计算欧式距离
    gl = array_len(groups)
    tmp = tile(in_x, (gl, 1)) - groups
    tmp = exponential_operation(tmp, 2)
    tmp = array_sum(tmp)
    tmp = exponential_operation(tmp, 0.5)

    # 得到排序后的数组的索引
    arg = argsort(tmp)

    # 计算最相似数据的前k个数据的分类次数
    cc = odict()
    for i in range(k):
        # 获得类别次数
        la = labels[arg[i]]
        cc[la] = cc.get(la, 0) + 1
    return max(cc) # 返回最相似数据的前k个数据中出现次数最多的分类作为新数据的分类

def main():
    groups, labels = load_data()
    in_x = [1.3, 2.1 ,3, 2.1]
    k = 3
    label = classify(in_x, groups, labels, k)
    print(label)

if __name__ == '__main__':
    main()




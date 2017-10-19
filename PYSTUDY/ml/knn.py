"""
knn近邻算法的简单编写
这个算法的精妙之处体现在计算距离，即计算新数据与数据集中的每个样本的相似度
计算相似度的方法有很多种，欧式距离其中一种，另外还有余弦，角度越小说明相似
度越高，越大，说明相似度越低，另外，角度的两边可以看做是两个样本的属性向量

另外，由于knn算法需要用新数据与数据集中的每个样本进行一一比较，所以，时间
复杂度比较高，不过，已经有人提出了分布式计算方案，后面学了，再一一道来；空
间复杂度也很高，因为要创建很大的样本集空间，所以系统内存会比较吃紧，比较少
的数据可以采用这个算法，数据量大的时候，要想想其它的方案。

最后，这个算法的精确度比较高。
"""
from PYSTUDY.numpylib import array, tile, argsort, array_sum, array_len, exponential_operation
from PYSTUDY.collectionslib import odict

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

"""
深度学习模块
"""
import tensorflow as tf

"""
随机数生成函数
"""
random_normal = tf.random_normal
"""
正态分布是具有两个参数μ和σ2的连续型随机变量的分布，第一参数μ是遵从正态分布的随机变量的均值，第二个参数σ2是此随机变量的方差，所以正态分布记作N(μ，σ2 )。 遵从正态分布的随机变量的概率规律为取μ邻近的值的概率大，而取离μ越远的值的概率越小；σ越小，分布越集中在μ附近，σ越大，分布越分散。
从正态分布中输出随机值。
参数:

    shape: 一维的张量，也是输出的张量。
    mean: 正态分布的均值。
    stddev: 正态分布的标准差。
    dtype: 输出的类型。
    seed: 一个整数，当设置之后，每次生成的随机数都一样。
    name: 操作的名字。
"""

truncated_normal = tf.truncated_normal
"""
从截断的正态分布中输出随机值。
生成的值服从具有指定平均值和标准偏差的正态分布，如果生成的值大于平均值2个标准偏差的值则丢弃重新选择。

在正态分布的曲线中，横轴区间（μ-σ，μ+σ）内的面积为68.268949%。
横轴区间（μ-2σ，μ+2σ）内的面积为95.449974%。
横轴区间（μ-3σ，μ+3σ）内的面积为99.730020%。
X落在（μ-3σ，μ+3σ）以外的概率小于千分之三，在实际问题中常认为相应的事件是不会发生的，基本上可以把区间（μ-3σ，μ+3σ）看作是随机变量X实际可能的取值区间，这称之为正态分布的“3σ”原则。
在tf.truncated_normal中如果x的取值在区间（μ-2σ，μ+2σ）之外则重新进行选择。这样保证了生成的值都在均值附近。

参数:

    shape: 一维的张量，也是输出的张量。
    mean: 正态分布的均值。
    stddev: 正态分布的标准差。
    dtype: 输出的类型。
    seed: 一个整数，当设置之后，每次生成的随机数都一样。
    name: 操作的名字
"""

"""
代码

a = tf.Variable(tf.random_normal([2,2],seed=1))
b = tf.Variable(tf.truncated_normal([2,2],seed=2))
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(a))
    print(sess.run(b))

输出：
[[-0.81131822  1.48459876]
 [ 0.06532937 -2.44270396]]
[[-0.85811085 -0.19662298]
 [ 0.13895047 -1.22127688]]
"""

random_uniform = tf.random_uniform

random_gamma = tf.random_gamma


"""
常数生成函数
"""
zeros = tf.zeros

ones = tf.ones

fill = tf.fill

constant = tf.constant


"""
常用矩阵运算函数
"""
matmul = tf.matmul


"""
变量
"""
Variable = tf.Variable
placeholder = tf.placeholder

"""
计算图
"""
Graph = tf.Graph


"""
会话
"""
Session = tf.Session

"""
数据类型
"""
float32 = tf.float32

# 跨维度的计算各张量的值
# 根据给出的axis在input_tensor上求平均值。除非keep_dims为真，
# axis中的每个的张量秩会减少1。如果keep_dims为真，求平均值的维度的长度都会保持为1.
# 如果不设置axis，所有维度上的元素都会被求平均值，并且只会返回一个只有一个元素的张量。
"""
import tensorflow as tf;
import numpy as np;

A = np.array([[1,2], [3,4]])

with tf.Session() as sess:
    # 整体求平均值
    print(sess.run(tf.reduce_mean(A)))
    # [2]
    # 按列求平均值
    print(sess.run(tf.reduce_mean(A, axis=0)))
    # [2, 3]
    # 按行求平均值
    print(sess.run(tf.reduce_mean(A, axis=1)))
    # [1, 3]
"""
reduce_mean = tf.reduce_mean


log = tf.log

"""
tf.clip_by_value(A, min, max)：输入一个张量A，
把A中的每一个元素的值都压缩在min和max之间。小于min
的让它等于min，大于max的元素的值等于max。
import tensorflow as tf;
import numpy as np;

A = np.array([[1,1,2,4], [3,4,8,5]])

with tf.Session() as sess:
    print sess.run(tf.clip_by_value(A, 2, 5))

输出:
[[2 2 2 4]
 [3 4 5 5]]
"""
clip_by_value = tf.clip_by_value

train = tf.train


# 初始化所有变量
global_variables_initializer = tf.global_variables_initializer



class NeuralNetworks(object):
    """
    神经网络
    """
    def example_load_data(self):
        """
        加载数据
        """
        # 特征向量
        self.x = constant([[0.7, 0.9]])

        # 权重向量, w1代表神经网络的第一层，w2代表神经网络的第二层
        self.w1 = Variable(random_normal([2, 3], stddev=1, seed=1))
        self.w2 = Variable(random_normal([3, 1], stddev=1, seed=1))

    def example_compute(self):
        """
        简单的神经网络实现前向传播的算法
        这里为什么能用矩阵乘法来计算呢？因为，通过求加权和发现
        正好是矩阵的乘法运算结果。所以，这里充分的体现了数学的美
        """
        a = matmul(self.x, self.w1)
        y = matmul(a, self.w2)

        sess = Session()
        sess.run(self.w1.initializer)
        sess.run(self.w2.initializer)
        print('第一种：', sess.run(y))
        sess.close()

    def example_2_load_data(self):
        """
        加载数据
        """
        # 权重向量, w1代表神经网络的第一层，w2代表神经网络的第二层
        self.w1 = Variable(random_normal([2, 3], stddev=1, seed=1))
        self.w2 = Variable(random_normal([3, 1], stddev=1, seed=1))
        # 特征向量, 区别是，这里不会在计算图中生成节点
        #self.x = placeholder(float32, shape=(1, 2), name='input')
        self.x = placeholder(float32, shape=(3, 2), name='input')

    def example_2_compute(self):
        """
        实现前向传播算法，减少计算图中节点的个数
        """
        a = matmul(self.x, self.w1) # 计算神经网络的第一层的输出向量
        y = matmul(a, self.w2) # 以第一层的输出作为第二层的输入再次计算第二层的输出

        sess = Session()
        initOp = global_variables_initializer() # 初始化所有变量
        sess.run(initOp)
        #print('第二种：', sess.run(y, feed_dict={self.x: [[0.7, 0.9]]}))
        print('第二种：', sess.run(y, feed_dict={self.x: [[0.7, 0.9], [0.1, 0.4], [0.5, 0.8]]}))
        sess.close()

    def evalute(self):
        """
        定义损失函数来刻画预测值与真实值的差距
        """
        """
        crossEntry = - reduce_mean(y * log(clip_by_value(y, 1e-10 1.0)))
        # 定义学习率
        learningRate = 0.001
        # 定义反向传播算法来优化神经网络中的参数
        trainStep = train.AdamOptimizer(learningRate).minimize(crossEntry)
        """
        pass


if __name__ == '__main__':
    """
    nn = NeuralNetworks()
    nn.example_load_data()
    nn.example_compute()

    nn1 = NeuralNetworks()
    nn1.example_2_load_data()
    nn1.example_2_compute()
    """
    pass

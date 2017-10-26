"""
深度学习模块
"""
import tensorflow as tf

"""
随机数生成函数
"""
random_normal = tf.random_normal

truncated_normal = tf.truncated_normal

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

"""
计算图
"""
Graph = tf.Graph


"""
回话
"""
Session = tf.Session

# 初始化所有变量
initialize_all_variables = tf.initialize_all_variables


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
        print(sess.run(self.w1))
        print(sess.run(self.w2))
        print(sess.run(a))
        print(sess.run(y))
        sess.close()


if __name__ == '__main__':
    nn = NeuralNetworks()
    nn.example_load_data()
    nn.example_compute()

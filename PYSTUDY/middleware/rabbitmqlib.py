"""
pika深度封装模块
"""
import pika
import traceback
from threading import Thread

class RabbitmqBase(object):
    """
    amqp连接基类
    """
    def __init__(self, user, passwd, host):
        """
        获得amqp连接和链道
        :param user: 用户名
        :param passwd: 密码
        :param host: 主机
        """
        credentials = pika.PlainCredentials(user, passwd)
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(
                host=host, credentials=credentials))
        self.ch = self.conn.channel()

    def close(self):
        try:
            self.ch.close()
            self.conn.close()
        except Exception as e:
            """
            这里是python的bug？还是什么原因，子类在删除的时候， 调用父类的方法时，
            居然找不到自己的属性，这和java不一样啊，越来越多的因素，感觉python非常
            不适合长期学习，你说是人不靠谱，这tmd子类清除的时候，父类没有这个属性。
            这里，我还遇到一个问题
            """
            print(e)


class _RabbitmqTask(Thread):
    """
    amqp任务线程类
    """
    def __init__(self, target, args, no_ack, ch, method, properties):
        """
        初始化
        :param target: 回调函数
        :param args: 回调函数参数
        :param no_ack: 是否允许不确认
        :param ch: 链道
        :param method:
        :param properties: 存储属性
        """
        super().__init__(target=target, args=args)
        self.no_ack = no_ack
        self.ch = ch
        self.method = method
        self.properties = properties

    def run(self):
        """
        线程启动
        :return:
        """
        super().run()
        if not self.no_ack:
            # 如果为True，任务结束后需要确认
            self.ch.basic_ack(delivery_tag=self.method.delivery_tag)
        
class RabbitmqCustomerMS(RabbitmqBase):
    """
    基于存储的消息队列的消费者
    """
    def __init__(self, user, passwd, host, prefetch_count, durable, no_ack,
                 task_queue, store_queue):
        """
        初始化
        :param user: 用户名
        :param passwd: 密码
        :param host: 主机
        :param prefetch_count: 最多同是进行多少个任务
        :param durable: 是否允许持久化任务
        :param no_ack: 是否需要确认，True则不需要确认
        :param task_queue: 任务队列名称
        :param store_queue: 存储数据的队列名称
        """
        super().__init__(user, passwd, host)

        self.task_queue = task_queue
        self.store_queue = store_queue
        self.prefetch_count = prefetch_count
        self.durable = durable
        self.no_ack = no_ack

    def send_task(self, body):
        """
        发送任务到任务队列
        :param body: 消息
        :return:
        """
        self.ch.basic_publish(exchange='', routing_key=self.task_queue,
            properties=pika.BasicProperties(delivery_mode=2), body=body)

    def store_data(self, data):
        """
        存储数据到存储队列
        :param data: 数据
        :return:
        """
        self.ch.basic_publish(exchange='', routing_key=self.store_queue,
            properties=pika.BasicProperties(delivery_mode=2), body=data)

    def serv_forever(self, func):
        """
        启动消费者服务程序
        :param func: 回调函数
        :return:
        """
        # 如果任务队列不为空则声明队列
        if self.task_queue:
            self.ch.queue_declare(
                queue=self.task_queue, durable=self.durable)
        if self.store_queue:
            self.ch.queue_declare(
                queue=self.store_queue, durable=self.durable)

        def callback(ch, method, properties, body):
            """
            amqp的回调函数
            :param ch: 链道
            :param method: 默认的方法
            :param properties: 默认
            :param body: 接收到的数据任务
            :return:
            """
            if self.prefetch_count > 1:
                # 如果任务队列的并发执行数大于1，则启动线程
                # 否则，单线程
                task = _RabbitmqTask(func, (self, body), self.no_ack, ch, method, properties)
                task.start()
            else:
                func(self, body)
                # 任务结束后，确认任务
                if not self.no_ack:
                    self.ch.basic_ack(delivery_tag=self.method.delivery_tag)

        # 声明队列
        self.ch.basic_qos(prefetch_count=self.prefetch_count)
        self.ch.basic_consume(callback, queue=self.task_queue, no_ack=self.no_ack)
        # 启动消费者
        self.ch.start_consuming()

class RabbitmqCustomerCus(RabbitmqBase):
    """
    自定义存储方式的消费者
    """
    def __init__(self, user, passwd, host, prefetch_count, durable, no_ack,
                 task_queue):
        """
        初始化
        :param user: 用户名
        :param passwd: 密码
        :param host: 主机
        :param prefetch_count: 最多同是进行多少个任务
        :param durable: 是否允许持久化任务
        :param no_ack: 是否需要确认，True则不需要确认
        :param task_queue: 任务队列名称
        """
        super().__init__(user, passwd, host)

        self.task_queue = task_queue
        self.prefetch_count = prefetch_count
        self.durable = durable
        self.no_ack = no_ack

    def store_data(self, body, callback):
        """
        存储数据
        :param body: 要存储的数据
        :param callback: 用于处理数据的回调函数
        """
        callback(body)

    def serv_forever(self, func):
        """
        启动消费者服务程序
        :param func: 回调函数
        :return:
        """
        # 如果任务队列不为空则声明队列
        if self.task_queue:
            self.ch.queue_declare(
                queue=self.task_queue, durable=self.durable)

        def callback(ch, method, properties, body):
            """
            amqp的回调函数
            :param ch: 链道
            :param method: 默认的方法
            :param properties: 默认
            :param body: 接收到的数据任务
            :return:
            """
            if self.prefetch_count > 1:
                # 如果任务队列的并发执行数大于1，则启动线程
                # 否则，单线程
                task = _RabbitmqTask(func, (self, body), self.no_ack, ch, method, properties)
                task.start()
            else:
                func(self, body)
                # 任务结束后，确认任务
                if not self.no_ack:
                    self.ch.basic_ack(delivery_tag=self.method.delivery_tag)

        # 声明队列
        self.ch.basic_qos(prefetch_count=self.prefetch_count)
        self.ch.basic_consume(callback, queue=self.task_queue, no_ack=self.no_ack)
        # 启动消费者
        self.ch.start_consuming()


class RabbitmqProducter(RabbitmqBase):
    """
    生产者
    """
    def __init__(self, user, passwd, host, task_queue, durable):
        """
        初始化
        :param user: 用户名
        :param passwd: 密码
        :param host: 主机名
        :param task_queue: 任务队列
        :param durable: 是否持久化
        """
        super().__init__(user, passwd, host)
        self.task_queue = task_queue
        self.durable = durable

    def send_task(self, body):
        """
        发送消息到任务队列
        :param body: 消息
        :return:
        """
        self.ch.basic_publish(exchange='', routing_key=self.task_queue,
            properties=pika.BasicProperties(delivery_mode=2), body=body)

    def produce(self, func):
        """
        启动生产者
        :param func: 生产者回调函数
        :return:
        """
        # 声明队列
        if not self.task_queue:
            self.ch.queue_declare(queue=self.task_queue, durable=self.durable)
        func(self)

"""
单元测试封装
"""
from unittest import TestCase, TextTestRunner, TestLoader, TestSuite, main

TestCase = TestCase # 测试单元类
run_all = main # 运行所有的测试单元

def run_test_case(testCase):
    """运行指定的testCase类
    :param testCase: 例如，A(TestCase), A即为参数
    """
    unit = TestLoader().loadTestsFromTestCase(testCase)
    TextTestRunner(verbosity=2).run(unit) 


def run_one_test(testCase, testMethod):
    """执行指定模块的指定测试方法
    :param testCase: 测试类
    :param testMethod: 测试方法
    """
    suite = TestSuite()
    suite.addTest(testCase(testMethod))
    TextTestRunner(verbosity=2).run(suite)

"""
单元测试封装
"""
from unittest import TestCase, TextTestRunner, TestLoader, main

TestCase = TestCase # 测试单元类
run_all = main # 运行所有的测试单元

def run_test_case(testCase):
    """运行指定的testCase类
    :param testCase: 例如，A(TestCase), A即为参数
    """
    unit = TestLoader().loadTestsFromTestCase(testCase)
    TextTestRunner(verbosity=2).run(unit) 

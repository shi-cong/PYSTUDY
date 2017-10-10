"""
ai 模块单元测试
"""

from unittest import TestCase
from test.example.human_model import train_human_model

class MSIBTestCase(TestCase):
    """
    贝叶斯分类模型单元测试
    """
    def test_human_msib(self):
        train_human_model()





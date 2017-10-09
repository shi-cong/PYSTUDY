"""
gpsspgapilib单元测试
"""

from unittest import TestCase
from shicong.gpsspgapilib import geo


class GpsspgapilibTestCase(TestCase):
    def test_geo(self):
        print(geo(*(22.616390222222222, 114.06048583333333)))
"""
gpsspgapilib单元测试
"""

from unittest import TestCase

from shicong.api.gpsspgapilib import geo


class GpsspgapilibTestCase(TestCase):
    def test_geo(self):
        print(geo(*(22.616567611111112, 114.05974577777778)))
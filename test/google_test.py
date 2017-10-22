"""
googleapilib 单元测试
"""
import import_module

from unittest import TestCase, main

from PYSTUDY.api.google import geocode


class GoogleTestCase(TestCase):
    def test_geocode(self):
        print(geocode(*(str(22.616390222222222), str(114.06048583333333))))
        

if __name__ == '__main__':
    main()

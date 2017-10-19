from unittest import TestCase
from PYSTUDY.encodelib import encode_unicode_url, decode_unicode_url


class EncodelibTestCase(TestCase):
    def test_decode_unicode_url(self):
        euu = encode_unicode_url({'a':'深圳'})
        print(euu)

        duu = decode_unicode_url('%E6%B7%B1%E5%9C%B3')
        print(duu)

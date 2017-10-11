"""
requestslib 单元测试
"""

from shicong.requestslib import HTTP

from unittest import TestCase
from shicong.oslib import write_image

class RequestslibTestCase(TestCase):
    def test_download_video(self):
        url = ""
        http = HTTP()
        headers = {}
        r = http.get(url, headers=headers, stream=True)
        filename = 'requestslib_data/a.mp4'
        write_image(r, filename)

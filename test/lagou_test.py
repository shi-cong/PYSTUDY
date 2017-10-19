from unittest import TestCase, main
from PYSTUDY.api.lagou import get_job_by_keyword

class LagouTestCase(TestCase):
    def test_tjl(self):
        """假设出现异常就表示是ip范文太频繁了。要等几天"""
        for jobs in get_job_by_keyword('python'):
            print(jobs)

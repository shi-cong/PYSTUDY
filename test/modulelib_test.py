from unittest import TestCase

import PYSTUDY.middleware.rabbitmqlib
from PYSTUDY.modulelib import get_curent_module_classes, is_subclass


class ModulelibTest(TestCase):
    def test_get_current_module_classes(self):
        print(get_curent_module_classes(PYSTUDY.middleware.rabbitmqlib))

    def test_is_subclass(self):
        print(is_subclass(PYSTUDY.middleware.rabbitmqlib.RabbitmqCustomer, PYSTUDY.middleware.rabbitmqlib.RabbitmqBase))

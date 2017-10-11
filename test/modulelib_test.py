from unittest import TestCase

import shicong.middleware.rabbitmqlib
from shicong.modulelib import get_curent_module_classes, is_subclass


class ModulelibTest(TestCase):
    def test_get_current_module_classes(self):
        print(get_curent_module_classes(shicong.middleware.rabbitmqlib))

    def test_is_subclass(self):
        print(is_subclass(shicong.middleware.rabbitmqlib.RabbitmqCustomer, shicong.middleware.rabbitmqlib.RabbitmqBase))

from shicong.modulelib import get_curent_module_classes, is_subclass
from unittest import TestCase
import shicong.rabbitmqlib


class ModulelibTest(TestCase):
    def test_get_current_module_classes(self):
        print(get_curent_module_classes(shicong.rabbitmqlib))

    def test_is_subclass(self):
        print(is_subclass(shicong.rabbitmqlib.RabbitmqCustomer, shicong.rabbitmqlib.RabbitmqBase))

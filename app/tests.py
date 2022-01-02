from django.test import TestCase
from .calc import add, subtract


class CalcTest(TestCase):

    def test_add_numbers(self):
        """Testcase for add function"""
        self.assertEqual(add(5, 9), 14)

    def test_subtract_numbers(self):
        self.assertEqual(subtract(5, 11), 6)

"""
This is the test suite for payroll1.py.
"""

from unittest import TestCase, skip

from code.payroll1 import calc_fed_inc

TEST_GROSS_INC = 1000


class PayrollTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_calc_fed_inc(self):
        self.assertLessEqual(calc_fed_inc(TEST_GROSS_INC), TEST_GROSS_INC)
        self.assertGreaterEqual(calc_fed_inc(TEST_GROSS_INC), 0)


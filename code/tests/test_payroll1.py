"""
This is the test suite for payroll1.py.
"""

from unittest import TestCase, skip

import code.payroll1 as pr

TEST_GROSS_INC = 1000


class PayrollTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_calc_bracketed_deduct(self):
        """
        We want to be sure the deduction is >= 0 and <= gross pay.
        """
        deduct = pr.calc_bracketed_deduct(TEST_GROSS_INC,
                                          pr.FED_TAX_BRACKETS)
        self.assertGreaterEqual(deduct, 0)
        self.assertLessEqual(deduct, TEST_GROSS_INC)
        deduct = pr.calc_bracketed_deduct(TEST_GROSS_INC,
                                          pr.PA_TAX_BRACKETS)
        self.assertGreaterEqual(deduct, 0)
        self.assertLessEqual(deduct, TEST_GROSS_INC)


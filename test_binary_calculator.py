import unittest

from bin_calc.arithmetic import (
    add_bin,
    sub_bin,
    mul_bin,
    div_bin
)
from bin_calc.conversions import (
    bin_to_dec,
    dec_to_bin
)

from bin_calc.validation import (
    is_binary_string,
    is_eight_bit_binary
)

class ValidationTests(unittest.TestCase):

    def test_valid_binary_string(self):
        self.assertTrue(is_binary_string("10101010"))

    def test_invalid_binary_string(self):
        self.assertFalse(is_binary_string("10201"))

    def test_valid_eight_bit_binary(self):
        self.assertTrue(is_eight_bit_binary("00000001"))

    def test_invalid_eight_bit_binary(self):
        self.assertFalse(is_eight_bit_binary("101"))


class ConversionTests(unittest.TestCase):

    def test_bin_to_dec(self):
        self.assertEqual(bin_to_dec("00100000"), 32)

    def test_dec_to_bin(self):
        self.assertEqual(dec_to_bin(32), "00100000")


class ArithmeticTests(unittest.TestCase):

    def test_add_bin(self):
        self.assertEqual(add_bin("00000001", "00000001"), "00000010")

    def test_add_bin_overflow_wraps_to_zero(self):
        self.assertEqual(add_bin("11111111", "00000001"), "00000000")

    def test_sub_bin(self):
        self.assertEqual(sub_bin("00000010", "00000001"), "00000001")

    def test_sub_bin_negative_not_supported(self):
        with self.assertRaises(ValueError):
            sub_bin("00000000", "00000001")

    def test_mul_bin(self):
        self.assertEqual(mul_bin("11111111", "11111111"), "1111111000000001")

    def test_div_bin(self):
        self.assertEqual(div_bin("101", "10"), ("10", "1"))

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div_bin("101", "0")


if __name__ == '__main__':
    unittest.main()
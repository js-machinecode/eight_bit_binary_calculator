import unittest
from bin_inverse.bin_inverse import bin_inverse

class BinInverseTests(unittest.TestCase):

#############
#Positive tests
#############

    def test_bin_inverse_zero(self):
        original_value = '0' * 8   # 0
        expected_value = '1' + '0' * 7 # -0
        inverse_value = bin_inverse(original_value)
        
        self.assertEqual(inverse_value, expected_value)

    def test_bin_inverse_positive_min_n(self):

    def test_bin_inverse_positive_small_n(self):

    def test_bin_inverse_positive_medium_n(self):

    def test_bin_inverse_positive_large_n(self):

    def test_bin_inverse_positive_max_n(self):

#############
#Negative tests
#############

    def test_bin_inverse_negative_min_n(self):

    def test_bin_inverse_negative_small_n(self):

    def test_bin_inverse_negative_medium_n(self):

    def test_bin_inverse_negative_large_n(self):
        original_value = '10111001'         # -71
        expected_value = '0'

        
    def test_bin_inverse_negative_max_n(self):
        original_value = '1' * 8            # -1
        expected_value = '0' * 7 + '1'      #  1

        self.assertEqual(original_value, expected_value)

#############
#Special case tests
#############

    def test_bin_inverse_twice_returns_original_n(self):
        original_value = '01011001'
        inverse_value = bin_inverse.bin_inverse(original_value)
        twice_inverse_value = bin_inverse.bin_inverse(inverse_value)
        
        self.assertEqual(twice_inverse_value, original_value)
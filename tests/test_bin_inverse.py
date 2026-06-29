import unittest
from bin_calc.bin_inverse import bin_inverse

class BinInverseTests(unittest.TestCase):

    def test_bin_inverse_zero(self):
        original_value = '0' * 8                                
        expected_value = '1' * 8                                
        inverse_value = bin_inverse(original_value)

        self.assertEqual(inverse_value, expected_value)

    def test_bin_inverse_min_n(self):
        original_value = '0' * 7 + '1'                          
        expected_value = '1' * 7 + '0'                                
        inverse_value = bin_inverse(original_value)

        self.assertEqual(inverse_value, expected_value)
 
    def test_bin_inverse_small_n(self):
        original_value = '0' * 5 + '111'                         
        expected_value = '1' * 5 + '000'                         
        inverse_value = bin_inverse(original_value)

        self.assertEqual(inverse_value, expected_value)
 
    def test_bin_inverse_medium_n(self):
        original_value = '01001011'                                 
        expected_value = '10110100'                                
        inverse_value = bin_inverse(original_value)

        self.assertEqual(inverse_value, expected_value)
  
    def test_bin_inverse_large_n(self):
        original_value = '01100111'                                   
        expected_value = '10011000'                                 
        inverse_value = bin_inverse(original_value)

        self.assertEqual(inverse_value, expected_value)
  
    def test_bin_inverse_max_n(self):
        original_value = '11111111'                                 
        expected_value = '0' * 8                        
        inverse_value = bin_inverse(original_value)

        self.assertEqual(inverse_value, expected_value)

#############
#Special case tests
#############

    def test_bin_inverse_twice_returns_original_n(self):
        original_value = '01011001'
        inverse_value = bin_inverse(original_value)
        twice_inverse_value = bin_inverse(inverse_value)
        
        self.assertEqual(twice_inverse_value, original_value)
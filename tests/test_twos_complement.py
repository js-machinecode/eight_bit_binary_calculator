from unittest import TestCase
from bin_calc.twos_complement import twos_complement
from bin_calc.bin_inverse import bin_inverse
from bin_calc.arithmetic import add_bin

class TwosComplementTests(TestCase):

    ONE = '00000001'


#############
#Positive tests
#############

    def test_twos_complement_zero(self):
        original_value = '0' * 8                               
        expected_value = add_bin(bin_inverse(original_value), self.ONE)
        resulted_value = twos_complement(original_value)
        self.assertEqual(resulted_value, expected_value)

    def test_twos_complement_positive_min_n(self):
        original_value = '0' * 7 + '1'                         
        expected_value = add_bin(bin_inverse(original_value), self.ONE)
        resulted_value = twos_complement(original_value)
        self.assertEqual(resulted_value, expected_value)
 
    def test_twos_complement_positive_small_n(self):
        original_value = '0' * 5 + '111'                       
        expected_value = add_bin(bin_inverse(original_value), self.ONE)
        resulted_value = twos_complement(original_value)
        self.assertEqual(resulted_value, expected_value)
 
    def test_twos_complement_positive_medium_n(self):
        original_value = '01001011'                            
        expected_value = add_bin(bin_inverse(original_value), self.ONE)
        resulted_value = twos_complement(original_value)
        self.assertEqual(resulted_value, expected_value)
  
    def test_twos_complement_positive_large_n(self):
        original_value = '01100111'                            
        expected_value = add_bin(bin_inverse(original_value), self.ONE)
        resulted_value = twos_complement(original_value)
        self.assertEqual(resulted_value, expected_value)
  
    def test_twos_complement_positive_max_n(self):
        original_value = '01111111'                            
        expected_value = add_bin(bin_inverse(original_value), self.ONE)
        resulted_value = twos_complement(original_value)
        self.assertEqual(resulted_value, expected_value)

#############
#Negative tests
#############

    def test_twos_complement_negative_min_n(self):
        original_value = '10000001'         
        expected_value = add_bin(bin_inverse(original_value), self.ONE)
        resulted_value = twos_complement(original_value)
        self.assertEqual(resulted_value, expected_value)

    def test_twos_complement_negative_small_n(self):
        original_value = '10000011'         
        expected_value = add_bin(bin_inverse(original_value), self.ONE)
        resulted_value = twos_complement(original_value)
        self.assertEqual(resulted_value, expected_value)

    def test_twos_complement_negative_medium_n(self):
        original_value = '10001101'         
        expected_value = add_bin(bin_inverse(original_value), self.ONE)
        resulted_value = twos_complement(original_value)
        self.assertEqual(resulted_value, expected_value)

    def test_twos_complement_negative_large_n(self):
        original_value = '11111100'         
        expected_value = add_bin(bin_inverse(original_value), self.ONE)
        resulted_value = twos_complement(original_value)
        self.assertEqual(resulted_value, expected_value)

    def test_twos_complement_negative_max_n(self):
        original_value = '1' * 8            # -1
        expected_value = add_bin(bin_inverse(original_value), self.ONE)
        resulted_value = twos_complement(original_value)
        self.assertEqual(resulted_value, expected_value)

#############
#Special case tests
#############

    def test_twos_complement_twice_returns_original_n(self):
        original_value = '01011001'
        first_operation = twos_complement(original_value)
        second_operation = twos_complement(first_operation)
        
        self.assertEqual(second_operation, original_value)
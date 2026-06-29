import unittest
from assignment_1 import dec_to_bin
from assignment_2 import bin_to_dec
from binary_calculator import add_bin
from binary_calculator import sub_bin
from binary_calculator import mul_bin
from binary_calculator import div_bin

from binary_calculator import mul_bin_shift_recursive

class BinaryCalculatorTests(unittest.TestCase):

##########################
#DECIMAL_TO_BINARY_CONVERSION
##########################

    def test_dec_to_bin_zero(self):
        result = dec_to_bin(0)
        self.assertEqual(result, '00000000')

    def test_dec_to_bin_one(self):
        result = dec_to_bin(1)
        self.assertEqual(result, '00000001')

    def test_dec_to_bin_two(self):
        result = dec_to_bin(2)
        self.assertEqual(result, '00000010')

    def test_dec_to_bin_four(self):
        result = dec_to_bin(4)
        self.assertEqual(result, '00000100')

    def test_dec_to_bin_eight(self):
        result = dec_to_bin(8)
        self.assertEqual(result, '00001000')

    def test_dec_to_bin_sixteen(self):
        result = dec_to_bin(16)
        self.assertEqual(result, '00010000')

    def test_dec_to_bin_thirty_two(self):
        result = dec_to_bin(32)
        self.assertEqual(result, '00100000')

    def test_dec_to_bin_sixty_four(self):
        result = dec_to_bin(64)
        self.assertEqual(result, '01000000')

    def test_dec_to_bin_128(self):
        result = dec_to_bin(128)
        self.assertEqual(result, '10000000')

    def test_dec_to_bin_255(self):
        result = dec_to_bin(255)
        self.assertEqual(result, '11111111')

    def test_dec_to_bin_five(self):
        result = dec_to_bin(5)
        self.assertEqual(result, '00000101')

    def test_dec_to_bin_ten(self):
        result = dec_to_bin(10)
        self.assertEqual(result, '00001010')

    def test_dec_to_bin_31(self):
        result = dec_to_bin(31)
        self.assertEqual(result, '00011111')

    def test_dec_to_bin_100(self):
        result = dec_to_bin(100)
        self.assertEqual(result, '01100100')

    def test_dec_to_bin_127(self):
        result = dec_to_bin(127)
        self.assertEqual(result, '01111111')

##########################
#BINARY_TO_DECIMAL_CONVERSION
##########################

    def test_bin_to_dec_zero(self):
        result = bin_to_dec('00000000')
        self.assertEqual(result, 0)


    def test_bin_to_dec_one(self):
        result = bin_to_dec('00000001')
        self.assertEqual(result, 1)


    def test_bin_to_dec_two(self):
        result = bin_to_dec('00000010')
        self.assertEqual(result, 2)


    def test_bin_to_dec_four(self):
        result = bin_to_dec('00000100')
        self.assertEqual(result, 4)


    def test_bin_to_dec_eight(self):
        result = bin_to_dec('00001000')
        self.assertEqual(result, 8)


    def test_bin_to_dec_sixteen(self):
        result = bin_to_dec('00010000')
        self.assertEqual(result, 16)


    def test_bin_to_dec_thirty_two(self):
        result = bin_to_dec('00100000')
        self.assertEqual(result, 32)


    def test_bin_to_dec_sixty_four(self):
        result = bin_to_dec('01000000')
        self.assertEqual(result, 64)


    def test_bin_to_dec_128(self):
        result = bin_to_dec('10000000')
        self.assertEqual(result, 128)


    def test_bin_to_dec_255(self):
        result = bin_to_dec('11111111')
        self.assertEqual(result, 255)

##########################
#BINARY_ADDITION
##########################

    def test_add_bin_no_carry(self):
        result = add_bin('00010000', '00000001')
        self.assertEqual(result, '00010001')

    def test_add_bin_one_carry(self):
        num1 = '00010000'
        desired_num = '00100000'
        result = add_bin(num1, num1)
        self.assertEqual(result, desired_num)

    def test_add_bin_multiple_carry(self):
        num1 = '10010011'
        num2 = '01010011'
        desired_num = '11100110'
        result = add_bin(num1, num2)
        self.assertEqual(result, desired_num)

    def test_add_bin_all_zeros(self):
        test_num = '00000000'
        result = add_bin(test_num, test_num)
        self.assertEqual(result, test_num)

    def test_add_bin_all_ones_v1(self):
        test_num = '11111111'
        desired_num = '11111110'
        result = add_bin(test_num, test_num)
        self.assertEqual(result, desired_num)

    def test_add_bin_all_ones_v2(self):
        num1 = '11111111'
        num2 = '00000000'
        result = add_bin(num1, num2)
        self.assertEqual(result, num1)

##########################
#BINARY_SUBTRACTION
##########################

    def test_sub_bin_zero_result(self):
        num1 = '00010001'
        desired_num = '0' * 8
        result = sub_bin(num1, num1)
        self.assertEqual(result, desired_num)

    def test_sub_bin_no_borrow(self):
        num1 = '00000101'
        num2 = '00000001'
        desired_num = '00000100'
        result = sub_bin(num1, num2)
        self.assertEqual(result, desired_num)

    def test_sub_bin_single_borrow(self):
        num1 = '00000100'
        num2 = '00000001'
        desired_num = '00000011'
        result = sub_bin(num1, num2)
        self.assertEqual(result, desired_num)

    def test_sub_bin_multiple_borrows(self):
        num1 = '00010000'
        num2 = '00000001'
        desired_num = '00001111'
        result = sub_bin(num1, num2)
        self.assertEqual(result, desired_num)

    def test_sub_bin_max_values_minus_one(self):
        num1 = '1' * 8
        num2 = '0' * 7 + '1'
        desired_num = '1' * 7 + '0'
        result = sub_bin(num1, num2)
        self.assertEqual(result, desired_num)

    def test_sub_bin_large_difference(self):
        num1 = '1' * 8
        num2 = '0' * 4 + '1' * 4
        desired_result = '1' * 4 + '0' * 4
        result = sub_bin(num1, num2)
        self.assertEqual(result, desired_result)

    def test_sub_bin_all_zeros(self):
        bin_num = '00000000'
        result = sub_bin(bin_num, bin_num)
        self.assertEqual(result, bin_num)


##########################
#BINARY_MULTIPLICATION
##########################

    def test_mul_bin_by_zero(self):
        result = mul_bin('00000101', '00000000')
        self.assertEqual(result, '0000000000000000')

    def test_mul_bin_by_one(self):
        result = mul_bin('11111111', '00000001')
        self.assertEqual(result, '0000000011111111')

    def test_mul_bin_simple(self):
        result = mul_bin('00000011', '00000010')
        self.assertEqual(result, '0000000000000110')

    def test_mul_bin_five_times_five(self):
        result = mul_bin('00000101', '00000101')
        self.assertEqual(result, '0000000000011001')

    def test_mul_bin_max_values(self):
        result = mul_bin('11111111', '11111111')
        self.assertEqual(result, '1111111000000001')

##########################
#RECURSIVE_BIT_SHIFT_MUL
##########################
    def test_mul_bin_shift_recursive_by_zero(self):
        result = mul_bin_shift_recursive('00000101', '00000000')
        self.assertEqual(result, '0000000000000000')


    def test_mul_bin_shift_recursive_zero_times_number(self):
        result = mul_bin_shift_recursive('00000000', '00000101')
        self.assertEqual(result, '0000000000000000')


    def test_mul_bin_shift_recursive_by_one(self):
        result = mul_bin_shift_recursive('11111111', '00000001')
        self.assertEqual(result, '0000000011111111')


    def test_mul_bin_shift_recursive_simple(self):
        result = mul_bin_shift_recursive('00000011', '00000010')
        self.assertEqual(result, '0000000000000110')


    def test_mul_bin_shift_recursive_five_times_five(self):
        result = mul_bin_shift_recursive('00000101', '00000101')
        self.assertEqual(result, '0000000000011001')


    def test_mul_bin_shift_recursive_power_of_two(self):
        result = mul_bin_shift_recursive('00001000', '00000100')
        self.assertEqual(result, '0000000000100000')


    def test_mul_bin_shift_recursive_larger_numbers(self):
        result = mul_bin_shift_recursive('00001101', '00001011')
        self.assertEqual(result, '0000000010001111')


    def test_mul_bin_shift_recursive_max_values(self):
        result = mul_bin_shift_recursive('11111111', '11111111')
        self.assertEqual(result, '1111111000000001')
##########################
#BINARY_DIVISION
##########################

    def test_div_bin_by_one(self):
        quotient, remainder = div_bin('11111111', '00000001')

        self.assertEqual(quotient, '11111111')
        self.assertEqual(remainder, '00000000')


    def test_div_bin_simple(self):
        quotient, remainder = div_bin('00001000', '00000010')

        self.assertEqual(quotient, '00000100')
        self.assertEqual(remainder, '00000000')


    def test_div_bin_with_remainder(self):
        quotient, remainder = div_bin('00000111', '00000010')

        self.assertEqual(quotient, '00000011')
        self.assertEqual(remainder, '00000001')


    def test_div_bin_zero_dividend(self):
        quotient, remainder = div_bin('00000000', '00000101')

        self.assertEqual(quotient, '00000000')
        self.assertEqual(remainder, '00000000')

    def test_div_bin_divisor_larger_than_dividend(self):
        quotient, remainder = div_bin('00000011', '00000101')

        self.assertEqual(quotient, '00000000')
        self.assertEqual(remainder, '00000011')

    def test_div_bin_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div_bin('00001000', '00000000')


if __name__ == '__main__':
    unittest.main()

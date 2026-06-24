# use the assignment_1.py and assignment_2.py to efficiently convert decimal numbers to binary and vice versa, 
# this file is performing as a calculator which handles user input. It also does Add, Subtract, Multiply, and Divide, as well as 
# 

import assignment_1
from assignment_1 import dec_to_bin_16
import assignment_2

def add_bin(num1, num2):
    '''
    inputs Str Str with each string being 8 characters in length and being a value of a binary number.
    returns the addition of the two binary numbers.
    TODO: Handle numbers over 255.
    '''
    carry = 0
    desired_bin = ''
    for bit in range(7, -1, -1):
        # test if both bits at the bit position are both 'on' and add the appropriate value to desired_bin and set the carry
        bit_1 = num1[bit]
        bit_2 = num2[bit]
        
        #print(f'bit_1: {bit_1}\nbit_2: {bit_2}\n')
        both_on = bool(int(bit_1)) and bool(int(bit_2))
        
        #print(f'both_on: {both_on}\n')
        both_off = int(bit_1) == 0 and (not bool(int(bit_2)))
        
        #print(f'both_off: {both_off}\n')
        if both_on:
            # check if we have a carry from the previous bit and add appropriately
            if carry:
                desired_bin = '1' + desired_bin
            else:
                desired_bin = '0' + desired_bin
            # this addition always results in a carry
            carry = 1
        # test if both bits at the bit position are 'off' oand add the appropriate value to desired_bin
        elif both_off:
            #don't forget carry
            if carry:
                desired_bin = '1' + desired_bin
            else:
                desired_bin = '0' + desired_bin
            carry = 0
        # otherwise if the both conditions above aren't true, we know that one or the other is 'on' and will add to desired_bin appropriately
        else:
            # don't forget the carry
            if carry:
                desired_bin = '0' + desired_bin
                carry = 1
            else:
                desired_bin = '1' + desired_bin
                carry = 0

        #print(f'desired_bin: {desired_bin}\n')
        
    return desired_bin

def sub_bin(num1, num2):
    '''
    inputs Str Str with each string being 8 characters in length and being a value of a binary number.
    returns the subtaction of the two binary numbers.
    TODO: Handle negative numbers
    '''
    desired_bin = ''

    borrow = 0
    for bit in range(7, -1, -1):
        bit1 = int(num1[bit])
        bit2 = int(num2[bit])

        # did we borrow from the previous bit?
        # then we must modify bit1 
        bit1 = bit1 - borrow

        if bit1 < bit2:
            # add 2 because we borrowed and we're in base 2
            bit1 += 2 
            borrow = 1
        else:
            borrow = 0
        
        # subtraction operation
        result_bit = bit1 - bit2

        # build our result
        desired_bin = str(result_bit) + desired_bin

    return desired_bin

#helper
def add_bin_any_length(num1, num2):
    '''
    inputs Str Str with both strings being representations of 16 bit binary number.
    returns the binary addition of num1 and num2.

    This helper is useful when we need more than 8 bits,
    such as a 16-bit multiplication result.
    '''

    carry = 0
    desired_bin = ''

    # Start from the rightmost bit and move left.
    for bit in range(len(num1) - 1, -1, -1):
        bit1 = int(num1[bit])
        bit2 = int(num2[bit])

        total = bit1 + bit2 + carry

        # The result bit is the remainder after dividing by 2.
        result_bit = total % 2

        # The carry is anything that moves into the next column.
        carry = total // 2

        desired_bin = str(result_bit) + desired_bin

    # If there is still a carry, place it at the front.
    if carry:
        desired_bin = '1' + desired_bin

    return desired_bin

def mul_bin(num1, num2):
    '''
    inputs Str Str with each string being 8 characters in length representing a 8 bit binary number.
    returns the multiplication of the two binary numbers as a 16-bit string.

    Example:
    00000011 * 00000010 = 0000000000000110
    '''

    # Convert both 8-bit numbers into 16-bit numbers.
    multiplicand = '00000000' + num1
    counter = num2

    # The largest result of 255 * 255 fits in 16 bits.
    result = '0000000000000000'

    # Multiplication can be viewed as repeated addition.
    # Example:
    # 3 * 4 = 3 + 3 + 3 + 3
    while counter != '00000000':

        # Add the multiplicand to the running 16-bit total.
        result = add_bin_any_length(result, multiplicand)

        # Keep only the rightmost 16 bits in case an extra carry appears.
        result = result[-16:]

        # Reduce the counter by one.
        counter = sub_bin(counter, '00000001')

    return result

#########################
#Tail-Recursive_Accumulator_VERSION_with_Bit_shifting
#########################

def mul_bin_shift_recursive(num1, num2):
    multiplicand = assignment_2.bin_to_dec(num1)
    multiplier = assignment_2.bin_to_dec(num2)

    return dec_to_bin_16(
        mul_shift_helper(multiplicand, multiplier, 0)
    )


def mul_shift_helper(multiplicand, multiplier, accumulator):
    '''
    Tail-recursive helper for binary multiplication.

    multiplicand:
        The number being repeatedly shifted left.

        Each left shift multiplies the multiplicand by 2,
        producing the next power-of-two multiple that may
        contribute to the final result.

    multiplier:
        The number being repeatedly shifted right.

        Each right shift moves to the next bit of the
        multiplier so we can determine whether the current
        power-of-two multiple should be included.

    accumulator:
        The running total of the multiplication.

        Whenever the current rightmost bit of the multiplier
        is 1, the current multiplicand is added to the
        accumulator.

        When the multiplier reaches zero, the accumulator
        contains the final product.
    '''

    # Base case:
    # If multiplier is zero, there are no more bits to process.
    if multiplier == 0:
        return accumulator

    # If the rightmost bit of multiplier is 1,
    # then essentially it is multiplication by 1,
    # and we know 1 times any number is that number,
    # thus we add the multiplicand that may or may not be
    # the original number we started with.
    if multiplier & 1:
        accumulator += multiplicand

    # Tail-recursive call:
    # - multiplicand << 1 means multiply multiplicand by 2
    # - multiplier >> 1 means move to the next multiplier bit
    # - accumulator carries the result so far
    return mul_shift_helper(
                            multiplicand << 1,
                            multiplier >> 1,
                            accumulator
                            )

def div_bin(num1, num2):
    '''
    inputs Str Str with each string being 8 characters in length
    returns the integer division of the two binary numbers.

    Example:
    00001000 / 00000010 = 00000100

    Current behavior:
    - Division by zero raises ZeroDivisionError.
    '''

    # Division by zero is undefined.
    if num2 == '00000000':
        raise ZeroDivisionError('Cannot divide by zero.')

    # Start the quotient at zero.
    quotient = '00000000'

    # The dividend becomes our working remainder.
    remainder = num1

    # Division can be viewed as repeated subtraction.
    # Example:
    # 8 / 2
    # 8 - 2 = 6
    # 6 - 2 = 4
    # 4 - 2 = 2
    # 2 - 2 = 0
    # We subtracted four times, so the answer is 4.
    # Division can be viewed as repeated subtraction.
    while bin_greater_equal(remainder, num2):

        # Remove one divisor from the remainder.
        remainder = sub_bin(remainder, num2)

        # Count how many successful subtractions occurred.
        quotient = add_bin(quotient, '00000001')

    # Return both results.
    return quotient, remainder

#helper function
def bin_greater_equal(num1, num2):
    '''
    returns True if binary num1 is greater than or equal to binary num2.
    assumes both numbers are valid 8-bit binary strings.
    '''

    # Compare bits from left to right.
    # The first differing bit determines which number is larger.
    for bit in range(8):

        # If num1 has a 1 where num2 has a 0,
        # num1 must be larger.
        if num1[bit] == '1' and num2[bit] == '0':
            return True

        # If num1 has a 0 where num2 has a 1,
        # num1 must be smaller.
        elif num1[bit] == '0' and num2[bit] == '1':
            return False

    # If every bit matched, the numbers are equal.
    return True

def main():
    while True:
        print("\nWelcome to the Decimal-Binary Calculator!")
        print("Please choose an option:")
        print("1. Convert Decimal to Binary")
        print("2. Convert Binary to Decimal")
        print("3. Add two binary numbers")
        print("4. Subtract two binary numbers")
        print("5. Multiply two binary numbers")
        print("6. Divide two binary numbers")
        print("7. Exit")

        choice = input("Enter your choice (1-7):")
        print()

        # 1. Convert Decimal to Binary
        if choice == '1':
            dec_num = input("Enter a decimal number (0-255): ")
            try:
                binary_result = assignment_1.dec_to_bin(int(dec_num))
                print(f"The binary representation of {dec_num} is: {binary_result}")
            except Exception as e:
                print("Something went wrong. Please try again.\n")
                continue

        #2. Convert Binary to Decimal
        elif choice == '2':
            bin_num = input("Enter a binary number (8 bits): ")
            try:
                decimal_result = assignment_2.bin_to_dec(bin_num)
                print(f"The decimal representation of {bin_num} is: {decimal_result}")
            except Exception as e:
                print("Something went wrong. Please try again.\n")
                continue

        elif choice in ['3', '4', '5', '6']:
            num1 = input("Enter the first binary number: ")
            num2 = input("Enter the second binary number: ")

            num1_is_bin = assignment_2.validate_bin_num(num1)
            num2_is_bin = assignment_2.validate_bin_num(num2)
            if (num1_is_bin and num2_is_bin):
                #3. Add two binary numbers      
                if choice == '3':
                    print(add_bin(num1, num2))

                #4. Subtract two binary numbers
                elif choice == '4':
                    print(sub_bin(num1, num2))
                #5. Multiply two binary numbers
                elif choice == '5':
                    print(mul_bin(num1, num2))    
                #6. Divide two binary numbers
                elif choice == '6':
                    quotient, remainder = div_bin(num1, num2)

                    print(f'Quotient : {quotient}')
                    print(f'Remainder: {remainder}')

                

            # print(f"The result of the {operation} is: {result}")

        elif choice == '7':
            print("Thank you for using the Decimal-Binary Calculator! Goodbye!\n")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.\n")


if __name__ == '__main__':
    main()
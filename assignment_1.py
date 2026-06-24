# Decimal to Binary function

def dec_to_bin(dec_num):
    '''dec_num is an int from 0 to 255 inclusive. 
    The function returns a string of 0s and 1s
    representing the binary representation of dec_num.'''
    # validating the input to ensure it is an integer from 0 to 255 inclusive.
    if dec_num < 0 or dec_num > 255:
        raise ValueError("Input must be an integer from 0 to 255 inclusive.")
    binary_representation = ""
    # calculating the bit value by right-shifting n by i positions and applying a bitwise AND with 1.
    for i in range(7, -1, -1):
        bit = (dec_num >> i) & 1    # This works by the bitwise right shift operator. It takes the binary
                                    # representation of n (our decimal in the range 0 to 255 inclusive)
                                    # and moves the bits by i positions, starting from the highest numeric
                                    # bit value (2^7) and moving down to the lowest bit value (2^0).
                                    # Once we get that bit value (essentially isolating the bit at position i),
                                    # we apply a bitwise AND with 1 to determine if that bit is 0 or 1.
        binary_representation += str(bit) # build our binary string starting from the left most bit to right most bit.
    return binary_representation

def dec_to_bin_16(num):
    '''
    Converts a decimal number into a 16-bit binary string.
    Used for multiplication because 255 * 255 = 65025.
    '''

    binary_representation = ''

    for i in range(15, -1, -1):
        bit = (num >> i) & 1
        binary_representation += str(bit)

    return binary_representation


# Example usage
if __name__ == "__main__":
    # # example 1
    # number = 10
    # print(f"The binary representation of {number} is: {dec_to_bin(number)}")

    # # example 2
    # number = 255
    # print(f"The binary representation of {number} is: {dec_to_bin(number)}")

    # # example 3
    # number = 0
    # print(f"The binary representation of {number} is: {dec_to_bin(number)}")

    print(f'186 in bin. is : {dec_to_bin(186)}') # 10111010
    print(f'78 in bin. is : {dec_to_bin(78)}') # 01001110
    print(f'55 in bin. is : {dec_to_bin(55)}') # 00110111

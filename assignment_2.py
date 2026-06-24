# binary string to decimal function

def validate_bin_num(bin_str):
    # validating the input to ensure it is a string of 8 bits (0s and 1s).
    if len(bin_str) != 8 or not all(bit in '01' for bit in bin_str):
        raise ValueError("Input must be a string of 8 bits (0s and 1s).")
    return True
    
def bin_to_dec(bin_str):
    '''binary_str is a string of 0s and 1s representing a single byte.
    The function returns the decimal representation of the binary number as an int.'''
    decimal_value = 0
    for i in range(8):
        # summing the binary string starting from the lowest numerical value.
        bit = int(bin_str[7 - i])
        decimal_value += bit * (2 ** i)
    return decimal_value

if __name__ == "__main__":
    # example 1
    binary_string = "00001010"
    print(f"The decimal representation of {binary_string} is: {bin_to_dec(binary_string)}")

    # example 2
    binary_string = "11111111"
    print(f"The decimal representation of {binary_string} is: {bin_to_dec(binary_string)}")

    # example 3
    binary_string = "00000000"
    print(f"The decimal representation of {binary_string} is: {bin_to_dec(binary_string)}")

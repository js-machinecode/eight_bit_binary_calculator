from bin_calc.type_defs import EightBitBinaryNumber

def bin_inverse(bin_str: EightBitBinaryNumber) -> EightBitBinaryNumber:
    '''Convert bin_str to it's opposite (one's complement)'''
    desired_bin_str = ''
    for bit in bin_str:
        flipped_bit = '1' if bit == "0" else '0'
        desired_bin_str += flipped_bit
    return desired_bin_str
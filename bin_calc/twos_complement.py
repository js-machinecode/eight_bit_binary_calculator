from bin_calc.type_defs import EightBitBinaryNumber
from bin_calc.arithmetic import add_bin
from bin_calc.bin_inverse import bin_inverse

ONE = '00000001'

def twos_complement(bin_str: EightBitBinaryNumber) -> EightBitBinaryNumber: 
    '''Add binary one to a eight bit binary number'''
    return add_bin(ONE, bin_inverse(bin_str))
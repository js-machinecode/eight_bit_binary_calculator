from bin_calc.type_defs import (
    BinaryNumber,
    EightBitBinaryNumber,
    DivisionResult,
    Quotient,
    Remainder,
)

def add_bin(
    num1: EightBitBinaryNumber,
    num2: EightBitBinaryNumber,
) -> EightBitBinaryNumber: ...

def sub_bin(
    num1: EightBitBinaryNumber,
    num2: EightBitBinaryNumber,
) -> EightBitBinaryNumber: ...

def mul_bin(num1: BinaryNumber, num2: BinaryNumber) -> BinaryNumber: ...

def div_bin(num1: BinaryNumber, num2: BinaryNumber) -> DivisionResult: ...
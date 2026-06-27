from bin_calc.type_defs import (
    BinaryNumber,
    EightBitBinaryNumber,
    DivisionResult,
    Quotient,
    Remainder,
)
from bin_calc.validation import (
    require_binary_string,
    require_eight_bit_binary,
)
from bin_calc.conversions import bin_to_dec, dec_to_bin


"""
Binary arithmetic operations.

This module contains the core arithmetic algorithms used
by the binary calculator.

Functions:
    add_bin()
    sub_bin()
    mul_bin()
    div_bin()
"""

def add_bin(
    num1: EightBitBinaryNumber,
    num2: EightBitBinaryNumber,
) -> EightBitBinaryNumber:
    """
    Add two 8-bit binary numbers.

    Parameters:
        num1: First binary operand.
        num2: Second binary operand.

    Returns:
        The 8-bit binary sum.

    Notes:
        Overflow is discarded.
    """
    require_eight_bit_binary(num1, "num1")
    require_eight_bit_binary(num2, "num2")

    carry = 0
    result = ""

    # Binary addition proceeds from right to left,
    # just as decimal addition does.
    for bit in range(7, -1, -1):
        bit1 = int(num1[bit])
        bit2 = int(num2[bit])

        # Sum both bits and any incoming carry.
        total = bit1 + bit2 + carry

        result_bit = total % 2

        # Any value larger than 1 produces a carry
        # for the next column.
        carry = total // 2

        result = str(result_bit) + result

    return result


def sub_bin(
    num1: EightBitBinaryNumber,
    num2: EightBitBinaryNumber,
) -> EightBitBinaryNumber:
    """
    Subtract one 8-bit binary number from another.

    Parameters:
        num1: Minuend.
        num2: Subtrahend.

    Returns:
        The binary difference.

    Raises:
        ValueError:
            If the subtraction would produce a
            negative result.
    """
    require_eight_bit_binary(num1, "num1")
    require_eight_bit_binary(num2, "num2")

    if bin_to_dec(num2) > bin_to_dec(num1):
        raise ValueError("negative binary subtraction is not supported")

    borrow = 0
    result = ""

    for bit in range(7, -1, -1):
        bit1 = int(num1[bit])
        bit2 = int(num2[bit])

        # Apply any borrow from the previous column.
        adjusted_bit1 = bit1 - borrow

        # Borrowing in binary adds 2 to the current
        # column and creates a borrow for the next.
        if adjusted_bit1 < bit2:
            adjusted_bit1 += 2
            borrow = 1
        else:
            borrow = 0

        result_bit = adjusted_bit1 - bit2
        result = str(result_bit) + result

    return result


def mul_bin(num1: BinaryNumber, num2: BinaryNumber) -> BinaryNumber:
    """
    Multiply two binary numbers using the
    shift-and-add algorithm.

    Parameters:
        num1: Multiplicand.
        num2: Multiplier.

    Returns:
        The binary product.
    """
    require_binary_string(num1, "num1")
    require_binary_string(num2, "num2")

    multiplicand = bin_to_dec(num1)
    multiplier = bin_to_dec(num2)
    product = 0


    # Shift-and-add multiplication:
    # Left shifts double the multiplicand.
    # Right shifts halve the multiplier.
    # Whenever the multiplier's least significant
    # bit is 1, the multiplicand contributes to
    # the final product.
    while multiplier > 0:
        # If the rightmost bit is 1, include the
        # current multiplicand in the product.
        if multiplier & 1:
            product += multiplicand

        # Equivalent to multiplying by 2.
        multiplicand <<= 1
        # Equivalent to integer division by 2.
        multiplier >>= 1

    return dec_to_bin(product, width=1)


def div_bin(num1: BinaryNumber, num2: BinaryNumber) -> DivisionResult:
    """
    Divide one binary number by another.

    Parameters:
        num1: Dividend.
        num2: Divisor.

    Returns:
        Tuple containing:
            quotient,
            remainder

    Raises:
        ZeroDivisionError:
            If divisor equals zero.
    """
    require_binary_string(num1, "num1")
    require_binary_string(num2, "num2")

    # Convert the binary representations into
    # decimal values so integer division can
    # be performed.
    dividend = bin_to_dec(num1)
    divisor = bin_to_dec(num2)

    if divisor == 0:
        raise ZeroDivisionError("cannot divide by zero")

    # Number of complete times the divisor fits
    # into the dividend.
    quotient: Quotient = dec_to_bin(dividend // divisor, width=1)
    # Value left over after division.
    remainder: Remainder = dec_to_bin(dividend % divisor, width=1)

    return dec_to_bin(quotient, width=1), dec_to_bin(remainder, width=1)
from bin_calc.type_defs import BinaryNumber, DecimalNumber
from bin_calc.validation import require_binary_string

"""
Binary and decimal conversion utilities.

This module provides functions for converting
between binary strings and decimal integers.
"""

def bin_to_dec(binary: BinaryNumber) -> int:
    """
    Convert a binary string into its decimal value.

    Example:
        "101" -> 5
    """
    require_binary_string(binary, "binary")

    total = 0

    for bit in binary:
        # Shift the accumulated value left by one place
        # and incorporate the next binary digit.
        total = total * 2 + int(bit)

    return total


def dec_to_bin(decimal: DecimalNumber, width: int = 8) -> BinaryNumber:
    if decimal < 0:
        raise ValueError("decimal must be non-negative")

    if width < 1:
        raise ValueError("width must be at least 1")

    if decimal == 0:
        return "0".zfill(width)

    result = ""

    while decimal > 0:
        result = str(decimal % 2) + result
        decimal //= 2

    return result.zfill(width)
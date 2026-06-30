"""
Input validation helpers.

This module verifies that values satisfy the
binary calculator data definitions.
"""

def is_binary_string(value: str) -> bool:
    """
    Determine whether a string represents a binary number.

    A valid binary string is non-empty and contains
    only the characters '0' and '1'.
    """
    return value != "" and all(bit in "01" for bit in value)


def is_eight_bit_binary(value: str) -> bool:
    return len(value) == 8 and is_binary_string(value)


def require_binary_string(value: str, name: str = "value") -> None:
    if not is_binary_string(value):
        raise ValueError(f"{name} must be a non-empty binary string")


def require_eight_bit_binary(value: str, name: str = "value") -> None:
    if not is_eight_bit_binary(value):
        raise ValueError(f"{name} must be an 8-bit binary string")
    


def is_hex_string(value: str) -> bool:
    '''
    Checks if value is a valid hex number.
    Valid hex numbers means it ranges from 0 - 9 and A - F (inclusive)
    '''
    hex_num_set = '0123456789ABCDEF'
    for elm in value:
        if elm not in hex_num_set:
            return False
    return True and value != ""


def require_hex_string(value: str, name: str = "value") -> None: 
    if not is_hex_string(value):
        raise ValueError(f"{name} must be a non-empty hex number inclusive string")
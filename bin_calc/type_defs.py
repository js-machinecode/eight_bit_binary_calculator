from typing import TypeAlias

BinaryNumber: TypeAlias = str
EightBitBinaryNumber: TypeAlias = str

DecimalNumber: TypeAlias = int

Quotient: TypeAlias = BinaryNumber
Remainder: TypeAlias = BinaryNumber

DivisionResult: TypeAlias = tuple[Quotient, Remainder]

HexNumber: TypeAlias = str
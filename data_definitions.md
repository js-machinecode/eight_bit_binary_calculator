# Data Definitions

## Purpose

This document defines the primary data used throughout the Binary Calculator project.

Data definitions answer the following questions:

* What does the data represent?
* How is the data represented in Python?
* What values are valid?
* What values are invalid?
* What constraints must always be true?

---

# BinaryNumber

## Purpose

Represents an unsigned binary value.

## Python Representation

```python
BinaryNumber = str
```

## Interpretation

A BinaryNumber is a string containing only binary digits.

Each digit represents a power of two.

Example:

```python
"101"
```

represents:

```text
1 × 2² + 0 × 2¹ + 1 × 2⁰

4 + 0 + 1

5
```

## Constraints

A BinaryNumber must:

* Be a string
* Be non-empty
* Contain only the characters `"0"` and `"1"`

## Valid Examples

```python
"0"
"1"
"10"
"101"
"11111111"
"1111111000000001"
```

## Invalid Examples

```python
""
"102"
"abc"
"10 01"
"-101"
```

---

# EightBitBinaryNumber

## Purpose

Represents an unsigned binary number stored using exactly eight bits.

## Python Representation

```python
EightBitBinaryNumber = str
```

## Interpretation

The leftmost bit is the most significant bit.

The rightmost bit is the least significant bit.

## Constraints

An EightBitBinaryNumber must:

* Satisfy all BinaryNumber requirements
* Contain exactly 8 characters

## Valid Examples

```python
"00000000"
"00000001"
"00000101"
"11111111"
```

## Invalid Examples

```python
""
"0"
"101"
"111111111"
"10200000"
```

## Usage

Addition and subtraction currently operate on EightBitBinaryNumber values.

---

# DecimalNumber

## Purpose

Represents a non-negative decimal integer.

## Python Representation

```python
DecimalNumber = int
```

## Constraints

A DecimalNumber must:

* Be an integer
* Be greater than or equal to zero

## Valid Examples

```python
0
1
5
32
255
1024
```

## Invalid Examples

```python
-1
-100
3.14
"10"
```

---

# DivisionResult

## Purpose

Represents the result of integer division.

## Python Representation

```python
DivisionResult = tuple[BinaryNumber, BinaryNumber]
```

## Structure

```python
(quotient, remainder)
```

## Example

```python
("10", "1")
```

Interpretation:

```text
5 ÷ 2

Quotient = 2
Remainder = 1
```

---

# Carry

## Purpose

Represents a carry generated during binary addition.

## Python Representation

```python
carry = int
```

## Valid Values

```python
0
1
```

## Interpretation

A carry value of 1 indicates that the previous column generated a value greater than 1.

Example:

```text
1 + 1 = 10
```

Result Bit:

```text
0
```

Carry:

```text
1
```

---

# Borrow

## Purpose

Represents a borrow generated during binary subtraction.

## Python Representation

```python
borrow = int
```

## Valid Values

```python
0
1
```

## Interpretation

A borrow value of 1 indicates that the current column borrowed from the next column to the left.

Example:

```text
0 - 1
```

requires borrowing.

---

# Multiplicand

## Purpose

Represents the value being repeatedly doubled during shift-and-add multiplication.

## Python Representation

```python
int
```

## Interpretation

Each left shift multiplies the multiplicand by two.

Example:

```text
5
10
20
40
```

---

# Multiplier

## Purpose

Represents the value being repeatedly halved during shift-and-add multiplication.

## Python Representation

```python
int
```

## Interpretation

Each right shift divides the multiplier by two.

Whenever the least significant bit is 1, the current multiplicand contributes to the final product.

---

# Product

## Purpose

Represents the final result of multiplication.

## Python Representation

```python
BinaryNumber
```

## Example

```python
mul_bin("11111111", "11111111")
```

returns:

```python
"1111111000000001"
```

---

# Dividend

## Purpose

Represents the value being divided.

## Python Representation

```python
BinaryNumber
```

---

# Divisor

## Purpose

Represents the value dividing the dividend.

## Python Representation

```python
BinaryNumber
```

## Constraints

The divisor must not represent zero.

## Invalid Examples

```python
"0"
"00"
"00000000"
```

Attempting division by zero raises:

```python
ZeroDivisionError
```

---

# Quotient

## Purpose

Represents the number of complete times a divisor fits into a dividend.

## Python Representation

```python
BinaryNumber
```

---

# Remainder

## Purpose

Represents the value left over after division.

## Python Representation

```python
BinaryNumber
```

---

# Validation Rules

Runtime validation is implemented in:

```text
bin_calc/validation.py
```

The primary validation functions are:

```python
is_binary_string(value)
is_eight_bit_binary(value)

require_binary_string(value)
require_eight_bit_binary(value)
```

## Design Principle

Data definitions describe what valid data means.

Validation functions enforce those rules.

Type aliases communicate those rules to developers and tooling.

Together they provide:

* Documentation
* Validation
* Maintainability
* Stronger software design

```
```

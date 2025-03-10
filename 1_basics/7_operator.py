#1.Arithmetic Operators:

print(5+6) # Addtion -> adding the numbers
print(5-6) # subtraction-> subtract the number
print(5*6) # Multiplication -> Multiply the number
print(5/2) # Divsion -> Divide the numnber
print(5//2) # Floor Division -> It trasform into integer number= 2.5 convert into 2
print(5%2) # Modulus -> It Provides remainder of the Divsion
print(5**2) # Exponential -> raising a number to a certain power.(raised to power)


#2. Comparison Operators:
# Comparison operators are used to compare two values and return a boolean result
#  Equal to (==)
#  Not equal to (!=)
#  Less than (<)
#  Greater than (>)
#  Less than or equal to (<=)
#  Greater than or equal to (>=)

print(5 == 6) # Equal -> It checks if two values are equal.
print(5 != 6) # Not Equal -> It checks if two values are not equal.
print(5 > 6) # Greater Than -> It checks if the left operand is greater than the right operand.
print(5 < 6) # Less Than -> It checks if the left operand is less than the right operand.
print(5 >= 6) # Greater Than or Equal To -> It checks if the left operand is greater than or equal to the right operand.
print(5 <= 6) # Less Than or Equal To -> It checks if the left operand is less than or equal to the right operand.


#3. Logical Operators:
# Logical operators are used to combine multiple conditions or values and return a boolean result.

#  and: Returns True if both conditions are true.
#  or: Returns True if at least one condition is true.
#  not: Returns True if the condition is false.

print(5 > 3 and 5 < 10) # and -> It returns True if both conditions are true.
print(5 > 3 or 5 < 3) # or -> It returns True if at least one condition is true.
print(not 5 > 3) # not -> It returns True if the condition is false.


#4. Assignment Operators:

# Assignment operators are used to assign values to variables.

#  =: Assigns the value of the right operand to the left operand.
#  +=: Adds the right operand to the left operand and assigns the result to the left operand.
#  -=: Subtracts the right operand from the left operand and assigns the result to the left operand.
#  *=: Multiplies the left operand by the right operand and assigns the result to the left operand.
#  /=: Divides the left operand by the right operand and assigns the result to the left operand.
#  //=: Performs floor division on the left operand by the right operand and assigns the result to the left operand.
#  %=: Computes the modulus of the left operand by the right operand and assigns the result to the left operand.
#  **=: Raises the left operand to the power of the right operand and assigns the result to the left operand.

x = 5
x += 3  # Equivalent to x = x + 3
print(x)  # Output: 8

x -= 2  # Equivalent to x = x - 2
print(x)  # Output: 6

x *= 2  # Equivalent to x = x * 2
print(x)  # Output: 12

x /= 3  # Equivalent to x = x / 3
print(x)  # Output: 4.0

x //= 2  # Equivalent to x = x // 2
print(x)  # Output: 2.0

x %= 2  # Equivalent to x = x % 2
print(x)  # Output: 0.0

x **= 2  # Equivalent to x = x ** 2
print(x)  # Output: 0.0


#5. Identity Operators:
# Identity operators are used to compare the memory locations of two objects.

#  is: Returns True if both variables point to the same object.
#  is not: Returns True if both variables do not point to the same object.

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is z)  # Output: True
print(x is y)  # Output: False
print(x is not y)  # Output: True
print(x is not z)  # Output: False

# bitwise operators
# 6. Bitwise Operators:
# Bitwise operators are used to perform bitwise operations on integers.

#  &: Bitwise AND: Sets each bit to 1 if both bits are 1.
#  |: Bitwise OR: Sets each bit to 1 if one of the bits is 1.
#  ^: Bitwise XOR: Sets each bit to 1 if only one of the bits is 1.
#  ~: Bitwise NOT: Flips the bits of the operand.
#  <<: Bitwise Left Shift: Shifts the bits of the operand to the left by a specified number of positions.
#  >>: Bitwise Right Shift: Shifts the bits of the operand to the right by a specified number of positions.


a = 5  # Binary: 101
b = 3  # Binary: 011

print(a & b)  # Output: 1 (Binary: 001)
print(a | b)  # Output: 7 (Binary: 111)
print(a ^ b)  # Output: 6 (Binary: 110)
print(~a)  # Output: -6 (Binary: 11111111111111111111111111111010)
print(a << 1)  # Output: 10 (Binary: 1010)
print(a >> 1)  # Output: 2 (Binary: 10)

#7. Membership Operators:
# Membership operators are used to check if a value is present in a sequence.

#  in: Returns True if the specified value is present in the sequence.
#  not in: Returns True if the specified value is not present in the sequence.

x = [1, 2, 3, 4, 5]

print(3 in x)  # Output: True
print(6 in x)  # Output: False

print(3 not in x)  # Output: False
# Output: True

#8. Ternary Operator:
# The ternary operator is a conditional expression that evaluates an expression based on a condition.

# Syntax: [on_true] if [expression] else [on_false]

x = 5
y = 10

max = x if x > y else y
print(max)  # Output: 10

#9. Operator Precedence:
# Operator precedence determines the order in which operators are evaluated in an expression.

# Operators with higher precedence are evaluated first.
# Parentheses can be used to control the order of evaluation.

# Arithmetic operators have higher precedence than comparison operators.
# Comparison operators have higher precedence than logical operators.
# Logical operators have higher precedence than assignment operators.

# Example:
# x = 5 + 3 * 2
# x = 5 + 6
# x = 11

# Example:
# x = 5 > 3 and 5 < 10
# x = True and True

# Example:
# x = 5 + 3 == 8
# x = 8 == 8
# x = True



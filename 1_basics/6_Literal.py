'''In Python, literals are used to represent fixed values in your code. These values are not
 variables or expressions but rather constants that have a specific value and data type
 associated with them. Python supports various types of literals'''
 
# 1. Numeric Literals: Numeric literals are used to represent numbers in Python. There are
# three types of numeric literals in Python: integers, floating-point numbers, and complex
# numbers.
# Integers: Integers are whole numbers without any decimal point. For example:
#   
# print(1234)  # Integer literal
#
# Floating-Point Numbers: Floating-point numbers are numbers that contain a decimal point.
# For example:
#
# print(3.14)  # Floating-point literal

# Complex Numbers: Complex numbers are numbers that have both a real and imaginary part.

print(5+6j)  # Complex number literal
# 2. String Literals: String literals are used to represent text in Python. Strings are enclosed
# in either single quotes (' ') or double quotes (" "). For example:

print("Hello, World!")  # String literal
print('Hello, World!')  # String literal

# 3. Boolean Literals: Boolean literals are used to represent the two truth values in Python:
# True and False. These values are used to represent logical conditions and are often used in
# conditional statements and expressions. For example:

print(True)  # Boolean literal
print(False)  # Boolean literal

# 4. None Literal: The None literal is used to represent the absence of a value or a null value in
# Python. It is often used to indicate that a variable has not been assigned a value or to

print(None)  # None literal

# 5. List Literals: List literals are used to represent lists in Python. Lists are ordered
# collections of values that can be of different data types. List literals are enclosed in square
# brackets [ ] and contain a comma-separated sequence of values. For example:

print([1, 2, 3, 4])  # List literal

# 6. Tuple Literals: Tuple literals are used to represent tuples in Python. Tuples are similar to
# lists but are immutable, meaning their contents cannot be changed after creation. Tuple
# literals are enclosed in parentheses ( ) and contain a comma-separated sequence of values.

print((1, 2, 3, 4))  # Tuple literal

# 7. Set Literals: Set literals are used to represent sets in Python. Sets are unordered

# collections of unique elements. Set literals are enclosed in curly braces { } and contain a
# comma-separated sequence of values. For example:

print({1, 2, 3, 4})  # Set literal

# 8. Dictionary Literals: Dictionary literals are used to represent dictionaries in Python.

# Dictionaries are collections of key-value pairs, where each key is associated with a value.
# Dictionary literals are enclosed in curly braces { } and contain a comma-separated sequence

# of key-value pairs, where the key and value are separated by a colon (:). For example:

print({"name": "Alice", "age": 30})  # Dictionary literal


a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal
#Float Literal
float_1 = 10.5 
float_2 = 1.5e2 # 1.5 * 10^2
float_3 = 1.5e-3 # 1.5 * 10^-3
 #Complex Literal 
x = 3.14j
print(a, b, c, d)
print(float_1, float_2,float_3)
print(x, x.imag, x.real)


# binary
x = 3.14j
print(x.imag)  # Output: 3.14

string = 'This is Python'
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\U0001f600\U0001F606\U0001F923"
raw_str = r"raw \n string"
print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)



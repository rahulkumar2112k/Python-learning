'''In Python, variables are used to store data values. These values can be numbers, strings,
 lists, dictionaries, or any other data type. Variables are essential for manipulating and
 working with data in your programs. Here's how you declare and use variables in Python:
 1. Variable Declaration: You declare a variable by assigning a value to it using the
 assignment operator '='
 
 1. Variable Names: Variable names (also known as identifiers) must adhere to the
 following rules:
 They can contain letters (a-z, A-Z), digits (0-9), and underscores (_).
 They cannot start with a digit.
 Variable names are case-sensitive, so myVar and myvar are treated as different
 variables.
 Python has reserved keywords (e.g., if, for, while, print) that cannot be used as variable
 names.
 1. Data Types: Python is dynamically typed, which means you don't need to declare the
 data type of a variable explicitly. Python will determine the data type automatically
 based on the assigned value. '''
 
x = 5  # 'x' is an integer variable
name = "Alice"  # 'name' is a string variable 

# 1. Reassignment: You can change the value of a variable by assigning it a new value.

x = 5
x = x + 1  # Updating the value of 'x' to 6

# 1. Multiple Assignments: You can assign multiple variables in a single line by separating
# the variable names with commas.

a, b, c = 5, 10, 15  # Assigning 5 to 'a', 10 to 'b', and 15 to 'c'

# 1. Swapping Variables: You can swap the values of two variables using a temporary

a=5
temp = a
a = b
b = temp  # Swapping the values of 'a' and 'b'


# 1. Constants: In Python, you can define constants by using uppercase variable names.
# Although Python does not have built-in support for constants, the convention is to
# use uppercase names to indicate that a variable should be treated as a constant.

PI = 3.14159  # 'PI' is a constant with the value 3.14159

# 1. Global vs. Local Variables: In Python, variables declared outside a function are
# considered global variables, while variables declared inside a function are considered
# local variables. Global variables can be accessed and modified from anywhere in the
# program, while local variables are limited to the scope of the function in which they are
# declared.



# 1. Variable Scope: The scope of a variable refers to the region of the program where the
# variable is accessible. In Python, variables have either global or local scope:
# Global variables are accessible from anywhere in the program.
# Local variables are only accessible within the function or block where they are
# declared.



#mutable and immutable data types
# 1. Mutable vs. Immutable: In Python, data types are classified as mutable or immutable:
# Mutable data types can be modified after creation, while immutable data types cannot be
# changed. For example:
# Lists and dictionaries are mutable data types, meaning you can add, remove, or modify
# elements after creation.
# Strings, tuples, and numbers are immutable data types, meaning you cannot change their
# contents after creation.
# Understanding the mutability of data types is essential for working with data in Python
# and can help you avoid unexpected behavior in your programs.

#mutable data type : list,set, dictionary ,bytearray,array   
#immutable data type : int, float,boolean,strings,tuples,frozenset,bytes

#eg

username="Rahul"

print(username) #output : Rahul

username="Rahul Kumar"

print(username) #output : Rahul Kumar 

# jab string immutable hai to phir username ko update kaise hua 
# hota kya hai jab python me koi bhi variable ka naam nahi hota hai
# jaise hi hum username="Rahul" likhte hai to python memory me ek object create karta hai
# jiska reference username variable me store hota hai

# jab hum username ko update karte hai to python memory me ek naya object create karta hai
# aur uska reference username variable me store hota hai
# purane object ko garbage collector delete kar deta hai
# isliye hume lagta hai ki humne variable ko update kiya hai

# ek aur example

x=10
y=x

print(x) #output : 10
print(y) #output : 10

x=20
print(x) #output : 20
print(y) #output : 10

# jab hum x=10 likhte hai to python memory me ek object create karta hai
# jiska reference x variable me store hota hai
# y=x se y variable me x variable ka reference store hota hai
# x=20 se python memory me ek naya object create hota hai
# jiska reference x variable me store hota hai
# y variable me x variable ka reference store hota hai
# isliye y variable ka value 10 hi rahta hai


    
      
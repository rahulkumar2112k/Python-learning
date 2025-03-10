
'''object types/data types
1. int
2. float
3. string
4. boolean

1. int
integer is a whole number, positive or negative, without decimals, of unlimited length.
Example: 7

2. float
Float is a number, positive or negative, containing one or more decimals.
Example: 7.0          

3. string
String is a sequence of characters enclosed in single or double quotes.
Example: "Hello, World!"

4. boolean
Boolean represents one of two values: True or False.
Example: True

In Python, we don't need to declare the type of variable. Python automatically assigns the data type according to the value assigned.'''


  
# Number :1234, 0, -1234, 3.4, 3.0, 3.4e5
# String : "Hello", 'Hello', "3"
# Boolean : True, False
# List : [1,2,3], ["a","b","c"]
# Tuple : (1,2,3), ("a","b","c")
# Set : {1,2,3}, {"a","b","c"}
# Dictionary : {"name":"John", "age":36}
# None : None

#Complex
print(5+6j)

#  6. List
#  In Python, a list is a data type used to store a collection of values. It is one of the built-in
#  data types and is classified as a sequence type. Lists are ordered, mutable (which means you
#  can change their contents), and can contain elements of different data types, including
#  integers, floats, strings, or even other lists.
#  You can create a list in Python by enclosing a comma-separated sequence of values within
#  square brackets [ ]. For example:
 
print([1,2,3,4])

#  7. Tuple
#  In Python, a tuple is another data type used to store a collection of values, similar to a list.
#  However, there are some key differences between tuples and lists:
#  Immutable: The most significant difference is that tuples are immutable, meaning once
#  you create a tuple, you cannot change its contents (add, remove, or modify elements).
#  Lists, on the other hand, are mutable, and you can modify them after creation.
#  Syntax: Tuples are created by enclosing a comma-separated sequence of values within
#  parentheses (). Lists are created with square brackets []. For example:
#  Performance: Due to their immutability, tuples can be more efficient in terms of
#  memory and performance for certain use cases compared to lists.
#  Tuples are often used when you have a collection of values that should not be changed
#  during the course of your program. For example, you might use tuples to represent
#  coordinates, dates, or other values that should remain constant.
#  You can create a tuple in Python by enclosing a comma-separated sequence of values
#  within parentheses (). For example:

print((1,2,3,4))

#  8. Set
#  In Python, a set is a data type used to store an unordered collection of unique elements.
#  Sets are mutable, meaning you can add or remove elements from them. However, sets do not
#  allow duplicate elements. When you create a set, Python automatically removes any
#  duplicate elements. Sets are useful for storing collections of unique values and performing
#  set operations such as union, intersection, difference, and symmetric difference.
#  You can create a set in Python by enclosing a comma-separated sequence of values within
#  curly braces {}. For example:
#  Note: If you try to create an empty set using empty curly braces {}, Python will create an
#  empty dictionary instead. To create an empty set, you can use the set() function.

print({1,2,3,4})   

#  9. Dictionary
#  In Python, a dictionary is a data type used to store a collection of key-value pairs. Dictionaries
#  are unordered, mutable, and can contain elements of different data types. Each key in a
#  dictionary must be unique, and the keys are used to access the corresponding values. You can
#  create a dictionary in Python by enclosing a comma-separated sequence of key-value pairs
#  within curly braces {}. Each key-value pair is separated by a colon :, with the key on the left
#  and the value on the right. For example:
#  The keys in a dictionary must be immutable, meaning they cannot be changed after they are
#  created. This is why you can use strings, numbers, or tuples as keys, but not lists or other
#  dictionaries.
#  Dictionaries are useful for storing data in a structured way and accessing values based on
#  their keys. You can use dictionaries to represent structured data such as user profiles,
#  configuration settings, or other key-value pairs.

print({"name":"John", "age":36})

#  10. None
#  In Python, None is a special constant used to represent the absence of a value or a null value.
#  None is often used to indicate that a variable or function does not have a value or has not been
#  initialized. You can think of None as a placeholder for a value that has not been defined yet.
#  None is a built-in constant in Python and is often used to initialize variables or return values
#  from functions when there is no meaningful value to return.
#  For example, if you have a function that performs some operation but does not return a value,
#  you can use the return statement with None to indicate that the function has completed
#  successfully but does not have a meaningful result to return.
#  You can assign None to a variable to indicate that the variable does not have a value. For
#  example:

x = None
print(x)

# How to know which type of Datatype is?
# You can use the type() function to determine the data type of a variable in Python. The type()
# function returns the data type of the specified variable. For example:

x = 5
print(type(x)) # Output: <class 'int'>
y = "Hello, World!"
print(type(y)) # Output: <class 'str'>
z = 20.5
print(type(z)) # Output: <class 'float'>
a = True
print(type(a)) # Output: <class 'bool'>
b = [1, 2, 3, 4]
print(type(b)) # Output: <class 'list'>
c = (1, 2, 3, 4)
print(type(c)) # Output: <class 'tuple'>
d = {1, 2, 3, 4}
print(type(d)) # Output: <class 'set'>
e = {"name": "John", "age": 36}
print(type(e)) # Output: <class 'dict'>
f = None
print(type(f)) # Output: <class 'NoneType'>



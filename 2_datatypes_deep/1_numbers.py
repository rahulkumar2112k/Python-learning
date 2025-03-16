# import math 

# math.floor(2.5) # 2
# math.floor(-2.5) # -3

# math.ceil(2.5) # 3
# math.ceil(-2.5) # -2

# math.trunc(2.5) # 2
# math.trunc(-2.5) # -2

# math.pow(2,3) # 8.0
# math.sqrt(16) # 4.0

# math.pi # 3.141592653589793

# math.e # 2.718281828459045

# math.inf # inf 

# # octal, hexadecimal, binary
# oct(10) # '0o12'

# hex(10) # '0xa'

# bin(10) # '0b1010'

# # use int() to convert them back to decimal

# int('0o12', 8) # 10
# int('0xa', 16) # 10
# int('0b1010', 2) # 10

# int ('64', 8) # 52
# int ('64', 16) # 100
# int ('64', 2) # 100

# # complex numbers
# complex(1,2) # (1+2j)

# # use .real and .imag to get real and imaginary parts
# c = complex(1,2)
# c.real # 1.0
# c.imag # 2.0

# x=2+3j
# x*2 # (4+6j)

# import random

# random.random() # random number between 0 and 1
# random.randint(1,10) # random integer between 1 and 10
# random.choice([1,2,3,4,5]) # random element from the list

# random.shuffle([1,2,3,4,5]) # shuffle the list

# random.seed(10) # set the seed to 10
# random.random() # 0.5714025946899135
# random.random() # 0.4288890546751146

# random.seed(10) # set the seed to 10
# random.random() # 0.5714025946899135

import decimal as d

# d.Decimal(10) # Decimal('10')

# d.Decimal('10.5') # Decimal('10.5')

# x=d.Decimal('0.1')+d.Decimal('0.1') -d.Decimal('0.2') # Decimal('0.0')

# print(x)

from fractions import Fraction
Fraction(1,3) # Fraction(1, 3)

x=Fraction(1,3)+Fraction(1,3) # Fraction(2, 3)

print(x)

# set

x = {1,2,3,4,5}
y = {4,5,6,7,8}

# z=x.union(y) # {1, 2, 3, 4, 5, 6, 7, 8}
# a=x.intersection(y) # {4, 5}

z=x&y
a=x|y

print(z)
print(a)    


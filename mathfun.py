#MATH.CEIL(X)
# '''Return the ceiling of x, the smallest integer greater than or eqaul to x. If x is not a float, delegates to
#    x.__ceil__() , which should return a Integral value.'''

import math
x=10.8
print(math.ceil(x))

print("------------__________")
# MATH.FABS(X)
#'''Return the absolute value of x.'''
x=-11
print(math.fabs(x))

print("------------__________")
# MATH.FACTORIAL(X)
# '''Return x factorial as an integer. Raises Value Error if x is not integral or is negative.'''
c=5
print(math.factorial(c))

print("------------__________")
# MATH.FLOOR(X)
# '''Return the floor of x, the largest integer less than or equal to x. If x is not a float, delegates to
#    x.__floor__(), which should return an integral value.'''
d=34.9
print(math.floor(d))

print("------------__________")
# MATH.FSUM(ITERABLE)
# '''Return an accurate floating point sum of values in the iterable.'''
l=[10,20,30,40]
print(math.fsum(l))

print("------------__________")
# MATH.SQRT(X)
# '''Return THE square root of x.'''
r=81
print(math.sqrt(r))

# https://docs.python.org/3.9/library/math.html
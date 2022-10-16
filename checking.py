import module1 as m

print(m.sum(10,20))
print(m.mul(10,20))

print("------------__________")
from module1 import *

print(sum(20,40))
print(mul(10,20))
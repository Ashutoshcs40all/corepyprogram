## '''PYTHON RANDOM randint() Method'''
# Return a number between 5 and 10 (both included):
# Import random
# print(random.randint(5,10))

## '''RETURNS A NUMBER BETWEEN 3(Included) and 9(Not Included)'''
# print(random.randrange(3,9))

## '''Python Random Choice() Method'''
# Return a random element from a list:
# i=["apple", "banana", "Mango"]
# print(random.choice(i))

import random
n=random.randint(2,8)
print(n)

print("------------__________")
n1=random.randrange(2,4)
print(n1)

print("------------__________")
l=[10, 20,30,40]
lc=random.choice(l)
print(lc)

print("------------__________")
# random()  :  Returns a random float number between 0 and 1
# shuffle   :  Takes a sequence and returns the sequence in a random order.
# uniform   :  Returns a random float number between two given parameters
r=random.random()
print(r)

print("------------__________")
l=[10, 20,30,40]
random.shuffle(l)
print(l)

print("------------__________")
u=random.uniform(3,9)
print(u)
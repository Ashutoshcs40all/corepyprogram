# A Tuple is a collection which is ordered and inmutable.
# Iterating through tuple is faster than with list.
t=(10,20,30,40,50,10,10)
print(type(t))

print("------------__________")
n=t[3]
print(n)

# ITERATING THROUGH A TUPLE
# Using a for loop we can iterate though each item in a tuple.
# Tuple function:- min(), max(), count(), index(), sum()
print("------------__________")
l=len(t)
for a in range(l):
    print(t[a])

print("------------__________")
for a in t:
    print(a)

print("------------__________")
m=min(t)
print(m)
print("------------__________")
m=max(t)
print(m)
print("------------__________")
c=t.count(10)
print(c)
print("------------__________")
c=t.index(50)
print(c)
print("------------__________")
s=sum(t,10)
print(s)
## A set is a collecion  which is unordered and unindexed , that is iterable, mutable, and has no duplicate elements.
# In python sets are written bu CURLY Brackets.

s=(10,20,30,40,50)
print(s)
print("------------__________")
for a in s:
    print(a)
print("------------__________")
a=[34,54,64,74,84,94]
b=set(a)
print(b)
#print("------------__________")
s1={10,20,30,40,50}
#s1.remove(20)
#print(s1)
#print("------------__________")
#s1.discard(40)
#print(s1)
print("------------__________")
#print(s1.pop())
#print(s1.pop())
#print(s1)
#print("------------__________")
#s1.clear()
#print(s1)
print("------------__________")
s1.add(60)
print(s1)
print("------------__________")
l=[11,21,31,41,10]
s1.update(l)
print(s1)

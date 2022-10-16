# list comprehension is an elegant way to define and create lists based on existing lists.
# list comprehension is generally more compact and faster than normal function and loops for creating list.
l=[]
for a in range(1,101):
    l.append(a)
print(l)

print("**********")

n=[m for m in  range(1,101) ]
print(n)

print("**********")

n=[m for m in  range(1,101) if m%2==0]
print(n)

print("**********")
s="ASHUTOSH"
d=[g for g in s]
print(d)
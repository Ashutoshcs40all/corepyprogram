#function for delete element from list:-
#del, pop(), remove(), clear()
l=[20,30,40,50,60]

del  l[1]
print(l)

print("&&&&&&")
print(l.pop(2))
print(l)

print("&&&&&&")
l.remove(60)
print(l)


print("&&&&&&")
l.clear()
print(l)

print("&&&&&&")
# update element from list:-
i=[20,30,50,60]
i[0]=90
print(i)


print("--------")
r=[20,30,50,60]
r.insert(0,10)
print(r)

print("________")
r=[20,30,50,60]
r.append(70)
print(r)


print("________")
n=[80,90]
p=[20,30,50,60]
p.append(n)
print(p)

print("________")
n=[80,90]
p=[20,30,50,60]
p.extend(n)
print(p)

l=[10,20,30,40,45]
l1=[2,3,4,98,89]

t=len(l)


for a,b in zip(l,l1):
    print(a,b)

print("**********")
for h in range(t):
    print(l[h],l1[h])

# PROGRAM TO CONVERT STRING TO A LIST

n=input("Enter the value")
print(n)
l=n.split();
print(l)

print("**********")
r=[]
for a in range(1,4):
    n=input("Enter The Value "+str(a)+":-")
    r.append(n)
    print(r)

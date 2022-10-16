d={
    'course':'python',
    'fees': 80000,
    'duration':'3 Months'
}
c=d.get('course')
c=d['course']
print(c)

print("*******")

for a in d.keys():
    print(a)

print("*******")
for b in d.values():
     print(b)

print("*******")
for e,f in d.items():
    print(e,f)

#print("*******")

#del d['fees']
#print(d)

#print("*******")
#print(d.pop('duration'))
#print(d)

print("*******")
g=dict(name='python',fees='40000')

print(g)

print("*******")
d.update({'fees':100000})
print(d)

#print("*******")
#d.clear()
#print(d)
print("*******")
d['desc']="This Is Python"
print(d)

print("*******")
d['fees']=20000
print(d)
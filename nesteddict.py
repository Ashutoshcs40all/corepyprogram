#"NESTED DICTIONARY"
# 1. Nested Dictionary means putting a dictionary inside another dictionary.
# 2. It's collection of dictionaries into one singal dictionary.

course={
      'php':{'duration':'3 months', 'fees': 15000 },
      'python':{'duration':'2 months', 'fees': 17000},
      'JAVA':{'duration':'4 months', 'fees': 25000},
}
print(course)
course['JAVA']['fees']=20000
print("-------------------")

print(course['php']['fees'])

print("-------------------")
for k,v in course.items():
      print(k,v['duration'],v['fees'])
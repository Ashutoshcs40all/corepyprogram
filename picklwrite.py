## '''THE PICKLE MODULE IMPLEMENTS A FINDAMENTAL, BUT POWERFUL ALGORITHM FOR SERIALZING
#     AND DE-SERIALIZING A PYTHON OBJECT STRUCTURE.'''
#     STORING DATA WITH PICKLE:-
# BOOLEANS, INTEGERS, FLOATS, COMPLEX NUMBERS, (NORMAL AND UNICODE)STRING, TUPLES, LISTS, SETS, AND DICTIONERS.
# TO USE PICKLE, START BY IMPORTING IT IN PYTHON
# '''pickle has two main methods. The first one is dump, which dumps an object to a file
#   object and then second one is load, which load an object from a file object.'''
#  PYTHON PICKLE FUNCTIONS
#  dump()- This function is called to serialize an object hierarchy.
#  load()- This function is called to de-serialize a data strem.


#  Pickling With Dump()
#'''Pickling data is done via the dump() function. It accepts data and a file
#   object. The dump()function then serializes  the data and writes it to the file. The syntax of dump() is as folows:
#    Syntax: dump(obj,file)'''

import pickle
l=[10,20,30,40]
file=open("writedata.txt","wb")
pickle.dump(l,file)
file.close()

print("------------__________")
#  UNPickling With load()
#'''The load() function takes a file object, reconstruct the objects from the pickled representation, and returns it.
#   The syntax is as folows:
#    Syntax: pickle.load(f)'''
file=open("writedata.txt","rb")
l=pickle.load(file)
print(l)
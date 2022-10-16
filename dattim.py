# import a module named datetime to work with dates as date objects.
# IMPORT DATETIME
# X= datetime.datetime.now()
# print(x)

## '''THE DATE CONTAINS YEAR, MONTH, DAY, HOUR, MINUTES, SECOND AND MICROSECOND.'''

# CREATING DATE OBJECTS
# x=datetime.datetime(2022,10,13)
# print(x)

import datetime

x = datetime.datetime.now()
print(x)
print(datetime.datetime(2022,2,22))

print("------------__________")
# '''PYTHON DATES'''
# he method is called strftime(), and takes one parameter,format, to specify the format of the returned string:
# %b : Month name, short version-------  Dec
# %B : Month name, Full version--------  December
# %m : Month as a number 01-12--------    12
# %M : Minute 00-59 ------  41
# %y : Year, short version, without century------ 18
# %Y : Year, full version--------  2018
# %H : Hour 00-23 -------    17
# %I : Hour 00-12------     05
# %p : AM/PM ----- PM
m =x.strftime("%p")
print(m)


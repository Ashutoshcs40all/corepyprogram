# '''A Function is a block of statments which can be used repetitively in program. it saves the time of a developer.
#    In Python concept of function is same as in other langauges. '''
# you can pass data, known as parameters, into a function.
## CREATNIG A FUNCTION:-
# IN PYTHON A FUNCTION IS DEFINED USING THE 'def' KEYWORD:

def showdata():
    print("Welcome In Lucknow")

showdata()
showdata()

print("------------__________")
#FUNCTION ARGUMENTS
# INFORMATION CAN BE PASSED TO FUNCTION AS PARAMETER
def sum(a,b):
    print(a+b)
sum(20,10)
sum(34,10)

print("------------__________")
#DEFAULT PARAMETER VALUE
def sum(a,b=1):
    print(a+b)
sum(20)
sum(34,30)

print("------------__________")
#RETURN VALUES
# TO LET A FUNCTION RETURN A VALUE, USE THE RETURN STATEMENT:
def square(x):
    return x*x,x*2
s=square(5)
print(s)

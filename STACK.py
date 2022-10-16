## IMPLEMENT A STACK AND QUEUE USING A LIST DATA TYPE
# THE STACK IS A LINEAR DATA STRUCTURE.
# STORES ITEMS IN A LIST-IN/FIRST-OUT (LIFO) OR FIRST-IN/LAST-OUT(FILO) MANNER.
# STACK OPERATION:-
#1. Push=>Inserting an Elements
#2. Pop=>Deletion An Element(Last Element)
#3. Peek=>Display the Last Element
#4. Display=>Display List

l=[]
while True:
    c=int(input('''
           1 Push Elemnts
           2 Pop Elemnts
           3 Peek Elemnts
           4 Display Stack
           5 Exit
           '''))
    if c==1:
        n=input("Enter The Value:-");
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Stack--")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("Empty Stack--")
        else:
            print("Last Stack Value:-",l[-1])
    elif c==4:
        print("Dispaly Stack:-", l)
    elif c==5:
        break;
    else:
        print("Invalid Opr.....")



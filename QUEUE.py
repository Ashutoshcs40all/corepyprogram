## The QUEUE is a linear data structure.
# Stores items in First In First Out(FIFO) manner.
# QUEUE OPERATION:-
#1. Enqueue: Adds an items to the queue.
#2. Dequeue: Removes an items from the queue.
#3. Front: Get the front item from Queue.
#4. Rear: Get the last item from queue.

l=[]
while True:
    c=int(input('''
           1 Push(Enqueue) Elemnts
           2 Pop(Dequeue) Elemnts
           3 Front Elemnts
           4 Rear(Last) Elemets
           5 Display Queue
           6 Exit
           '''))
    if c==1:
        n=input("Enter The Value:-");
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Queue--")
        else:
            del l[0]
            print(l)
    elif c==3:
        if len(l)==0:
            print("Empty Queue--")
        else:
            print("First Queue Value:-",l[0])
    elif c==4:
        if len(l) == 0:
            print("Empty Queue--")
        else:
            print("Last Queue Value:-", l[-1])
    elif c==5:
        print("Display Queue",l)
    elif c==6:
        break;
    else:
        print("Invalid Opr.....")
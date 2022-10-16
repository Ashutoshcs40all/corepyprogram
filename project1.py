## '''NUMBER GUESSING GAME PYTHON(USING RANDOM MODULE) '''
import random

Cnumber= random.randrange(1,101)
userInput=int(input("Enter your Number:-"))
if userInput>Cnumber:
    print("Computer Number:-", Cnumber)
    print("Your Guess Number is too High. ")
elif userInput<Cnumber:
    print("Computer Number:- ", Cnumber)
    print("Your Guess Number is too Low. ")
else:
    print("Computer Number:- ", Cnumber)
    print("Your Guess Number is Equal. ")

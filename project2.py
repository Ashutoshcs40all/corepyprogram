## '''ROCK PAPER SCISSORS GAME(USING RANDOM MODULE)'''
# ''' WINNING RULES AS FOLLOWS:
# ROCK vs PAPER-> paper wins
# ROCK vs SCISSOR-> rock wins
# PAPER vs SCISSOR-> scissor wins'''

import random
l=["Rock", "Scissor", "Paper"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
    Game Start.....
    1 YES
    2 NO/EXIT
    '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
            1 ROCK
            2 SCISSOR
            3 PAPER
            '''))
            if userInput==1:
                uchoice="Rock"
            elif userInput==2:
                uchoice="Scissor"
            elif userInput==3:
                uchoice="Paper"

            Cchoice=random.choice(l)
            print(uchoice)
            print(Cchoice)
            if Cchoice==uchoice:
                print("Computer Value:-",Cchoice)
                print("User Value:-",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="Rock" and Cchoice=="Scissor") or (uchoice=='Paper' and Cchoice=="Rock") or (uchoice=="Scissor" and Cchoice== "Paper"):
                print("Computer Value:-", Cchoice)
                print("User Value:-", uchoice)
                print("You Win")
                ucount=ucount+1
            else:
                print("Computer Value:-", Cchoice)
                print("User Value:-", uchoice)
                print("Computer Win")
                ccount=ccount+1

        print("------------__________")
        if ucount==ccount:
            print("Final Game Draw......")
            print("User Score",ucount)
            print("Computer Score",ccount)
        elif ucount>ccount:
            print("Final You Win The Game ......")
            print("User Score", ucount)
            print("Computer Score", ccount)
        else:
            print("Final Computer Win The Game ......")
            print("User Score", ucount)
            print("Computer Score", ccount)

    else:
        break


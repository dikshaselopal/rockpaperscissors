" rock ,paper and scissors game "
import random
list1=['rock','paper','scissors']
gameOver=True
while(gameOver):
    play=input("Press Enter=To play.\nQ-to Quit.")
    if(play=='Q' or play=='q'):
         gameOver=False
    else:
        print('''"welcome to rps"''')
        user=input('''" Enter any word from rock, paper & scissors: " ''')
        rock,paper,scissors='rock','paper','scissors'
        computerchoice= random.choice(list1)
        print(computerchoice)
        if(user=='rock' and computerchoice=='paper'):
         print("computer wins")
        elif(user=='paper' and computerchoice=='scissors'):
         print( "computer wins")
        elif(user=='scissors' and computerchoice== 'rock'):
         print("you won")
        elif(user=='rock' and computerchoice=='scissors' ):
         print("you won")
        elif(user=='scissors' and computerchoice=='paper'):
         print("you won")
        elif(user=='paper' and computerchoice=='rock'):
         print("you won")
        elif(user== computerchoice):
         print("draw")
        else:
         print("bad luck")

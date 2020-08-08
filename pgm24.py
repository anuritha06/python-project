#rock paper scissor game

import random

print("welcome to the game of rock, paper, scissor")

while True:
    play=input("do you want to start the game? type y for yes and n for no")
    if play=='y' or play=='Y':
        var1=input("enter rock, paper, or scissor : ")
        lst=['rock','paper','scissor']
        random.shuffle(lst)
        var2=lst.pop()
        if var1=='paper':
            if var2=='paper':
                print("paper generated :its a draw")
            elif var2=='rock':
                print("rock generated : you lost")
            else:
                print("scissor generated : you won")
        elif var1=='rock':
              if var2=='paper':
                  print("paper generated : you won")
              elif var2=='rock':
                  print("rock generated : its a draw")
              else:
                  print("scissor generated : you lost")
        if var1=='scissor':
             if var2=='paper':
                 print("paper generated : you lost")
             elif var2=='rock':
                 print("rock gennerated : you won")
             else:
                 print("scissor generated : its a draw")
             
            
    
    

             
            
    
    

'''
Stone Paper Scissor Game
rule
1 for stone
0 for paper 
-1 for scissor

'''

import random

computer = random.randint(-1,1)
print("1 for stone, 0 for paper , -1 for scissor :")
user = int(input("Choose your type : "))
print(computer)

dict = {1:"Stone", 0:"Paper", -1:"Scissor"}
print(f"You choosed {dict[user]}  & Computer choosed {dict[computer]}")

if computer == user :
    print("It's a draw")

else :
    if computer == 1 and user == 0:
        print("You won")
    elif computer == 1 and user == -1:
        print("You Loose")    
    elif computer == 0 and user == 1:
        print("You Loose") 
    elif computer == 0 and user == -1:
        print("You Won")     
    elif computer == -1 and user == 1:
        print("You Won")
    elif computer == -1 and user == 0:
        print("You Loose")  
            

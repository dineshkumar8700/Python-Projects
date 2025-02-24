'''
Snake Water Gun Game
1 for snake
-1 for water
0 for gun

'''

import random
computer = random.choice([-1, 1, 0])

userDict = {"s":1, "w":-1, "g":0}
reversedDict = {1:"Snake", -1:"Water", 0:"Gun"}

userInput = input("Enter your choice s for snake, w for water and g for gun : ")
user = userDict[userInput]

print(f"You choosed : {reversedDict[user]}")
print(f"Computer choosed : {reversedDict[computer]}")

if user == computer :
    print("It's a draw")
else :
    if user == 1 and computer == -1 :
        print("You won!")    
    elif user == 1 and computer == 0 :
        print("You Lose!")
    elif user == -1 and computer == 0 :
        print("You Won!")
    elif user == -1 and computer == 1 :
        print("You Lose!")
    elif user == 0 and computer == 1 :
        print("You Won!")
    elif user == 0 and computer == -1 :
        print("You Lose!")
    else :
        print("Something Went wrong")        

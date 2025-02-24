name = input("Enter your name : ")
print(f"Welcome {name} to the adventure ")

answer = input("You have 2 option go right or left to explore the game choose one (right/left)").lower()

if answer == "left":
    answer = input("You come across a rive, you have 2 option either swim of walk accross it. (swim/walk)").lower()
    if answer == "swim" :
        print("You are eaten by crocodile. You lose the game... Try again")
    elif answer == "walk":
        print("You walked miles and ran out of water.. You lose the game. Try again")
    else:
        print("Invalid opetion. You loose") 

elif answer == "right":
    answer = input(("You come across a bridge which is very old and may break if you go through it. You have 2 option go back or cross it (back/cross)")).lower()
    if answer == "back" :
        print("You afraid. You lose the game... Try again")
    elif answer == "cross":
        print("You crossed the bridge")
        answer = input(("Now you come accross a stranger man. Would you like to talk to hime he may also kill you because he has a knife (yes/no)")).lower()
        if answer == "yes":
            print("He gave you gold and you win")
        elif answer == "no":
            print("You afraid. You lose the game... Try again")        
        else:
            print("Invalid opetion. You loose")         
    else:
        print("Invalid opetion. You loose") 

else:
    print("Invalid opetion. You loose")    

print("Thankyou for playing")
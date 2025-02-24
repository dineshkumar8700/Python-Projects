# Answer the Question and record the total marks gained

print("Welcome to Answer the Questions Game !")
print("Answer each question and get one mark for each..")

score = 0
answer = input("Q.1 What is the full form of RAM ? ")
if answer.lower() == "random access memory" :
    print("Correct Answer !")
    score += 1
else :
    print("Wrong Answer !")

answer = input("Q.2 What is the full form of ROM ? ")
if answer.lower() == "read only memory" :
    print("Correct Answer !")
    score += 1
else :
    print("Wrong Answer !")    

answer = input("Q.3 What is the full form of CPU ? ")
if answer.lower() == "central processing unit" :
    print("Correct Answer !")
    score += 1
else :
    print("Wrong Answer !")

answer = input("Q.4 What is the full form of OS ? ")
if answer.lower() == "operating system" :
    print("Correct Answer !")
    score += 1
else :
    print("Wrong Answer !")    

answer = input("Q.5 What is the full form of AI ? ")
if answer.lower() == "artificial intelligence" :
    print("Correct Answer !")
    score += 1
else :
    print("Wrong Answer !")

print("End of game...")
print(f"Your score is {score} out of 5 and percentage is {(score/5)*100}")    
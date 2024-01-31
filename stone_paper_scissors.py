import random

count_comp=0
count_user=0

options=['rock','paper','scissor']

while True:
    user_guess = input("choose rock, paper, scissor or q to quit :").lower()
    if user_guess == "q":
        break
    if user_guess not in options:
        print("select the valid options only")
        continue
    comp_guess= options[random.randint(0,2)]
    print(comp_guess)

    if comp_guess == "rock" and user_guess == "paper":
        print("you won")
        count_user+=1
    
    elif comp_guess == "scissor" and user_guess == "rock":
        print("you won")
        count_user+=1

    elif comp_guess == "paper" and user_guess == "scissor":
        print("you won")
        count_user+=1

    elif comp_guess == user_guess:
        print("tie")
        continue

    else:
        print("computer won")
        count_comp+=1

print("your score is :"+ str(count_user)+ " computer score is :" +str(count_comp))
if count_comp == count_user:
    print("match tie")
if count_comp > count_user:
    print("match won by coumpter")
else:
    print("match won by you")        

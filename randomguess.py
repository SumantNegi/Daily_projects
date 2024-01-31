import random

max = int(input("enter the maximum range to guess :"))

if max <=0:
    print ("minimum must be greater than 0")
    quit()

else :
    print ("the number will be between "+ str(max))    

random_no = random.randint(0,max)
print(random_no)    

guess = int(input("enter the guess "))
if guess == random_no:
    print("correct guess")
else:
    while (guess!=random_no):
        if guess<random_no:
            print("number is greater than your guess")
            guess= int(input("enter new guess :"))
        else:
            print("number is smaller than your guess")
            guess= int(input("enter new guess :"))
        continue
    if guess == random_no:
        print("correct guess")
        
    
        
    

print ("hello.... user")

ans = input ('do you want to play quiz? ')

if ans.lower() !="yes" :

    quit()

else : 
    print('let start')

count =0
ans1 = input("total no of continents are? ")
if ans1 == "7":
    count+=1
    print ("correct")
    # in python count++ not work
else:
    print("incorrect") 

ans2 = input("total no of players in cricket team are :")
if ans2 == "11":
    print ("correct")
    count+=1
else:
    print("incorrect")

ans3 =input("india prime minster is ? ").lower()
if "modi" in ans3: # you can find substring in stirng in python
    print("correct")
    count+=1
else:
    print("incorrect")

print("your total score is : "+str(count))    





    


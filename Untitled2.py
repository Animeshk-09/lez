#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
Objective: Program to implement GUESS THE NUMBER game . 
           The user is given 5 chances to guess a number in the range 10<=number<=50.
           
           If the user's guess matches the number generated , 
           Python displays 'YOU WIN ' and the loop terminates without completing the five iteration.
           
           If however , cannot guess the number in five attempts, python displays 'YOU LOSE'.
           
Input Parameter: integer value between [10,50]
return value : string
'''


import random
number=random.randint(1,100)
c=0
while c<5:
    guess = int(input("Guess a number in range 1..100:"))
    if guess == number:
        print("YOU WIN!!:)")
        
        break
    else:
        c+=1
        if guess < number:
            print("the correct number is greater than the entered number")
            
        else :
            print("correct number is smaller than entered number")
if not c<5:
    print("YOU LOSE :(\n The number was", number)
    


# In[ ]:







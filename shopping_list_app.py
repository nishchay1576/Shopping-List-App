# -*- coding: utf-8 -*-
# Shopping List App 

"""
    We are going to make a "Shopping List" app. 
    Run the script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT 
    the program
    And once i quit, I want the app to show me 
    everything thats
    on my list.

Hint:
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use 
    the app

    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app with DONE

    Step 6: print out the list
"""
shopping_list = [] #Made a list
#INSTRUCTIONS
print ('What should we pick up at the store ?')
print ('Enter DONE to stop addding items.')

while(True): #Ask for New items
    x = input('Add item :')
    
    if(not x):
        print('Enter correct Details')
        continue
    if(x == 'DONE'): #Able to quit th app with DONE
        break
    
    shopping_list.append(x) #Add new items to list
    
print("Here's your list")
for x in shopping_list:
    print(x)


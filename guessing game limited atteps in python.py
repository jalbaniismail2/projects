'''
Assignment 7 - 27 November 2025 
7.	Create a number-guessing game where the user has a limited number of attempts to guess a random number. Let you have 3 attempts, at every guess attempt, if you attempt wrongly, the program should show the remaining number of attempts.



EXTRA BY ME :    USER CHOICE ATTEMPTS
'''



import random

selected_number=random.randint(1,100)



#print message on console that program has selected a number!
print("Hey! I have selected a number can you guess it?   ")

#generate a new line
print()



# set upper level for Attempts
attempt_number=int(input("Enter Attempt Number Upper Range (Numbr Must be greater than 0 :"))

#generate a new line
print()


#print message for total attempts
print("You have total appempts  ", attempt_number)


#generate a new line
print()




# loop 1 to range of attempt number
i=1
while i <= attempt_number :

    #print remaining attempts
    print(f"Your Remaining Attempts:  {attempt_number}")
    #generate a new line
    print()
    #decrease attempt Limit by one
    attempt_number-=1

    
    #generate a new line
    print()
    # print a message to the user to  guess the Selected Number
    guess=int(input("Enter your guess?  "))


    #condition if guess is less than  Selected number
    if guess < selected_number :
        print(f"oh! Your guess {guess} is less than Selected_number !")


    #elif the guess it greater than Selected number
    elif guess > selected_number :
        print(f"Oh! Your guess {guess} is greate than Selected_Number!")


    #elif guessed the number
        
    else:
        print(f"Hurry! You guessed the Number:  {guess} !")
        break






#if the attempt number ends (loop stops iteration) program should display

else:
    print("Oh! Your Attemp Limit is ", attempt_number,"!")


        


        

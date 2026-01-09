'''Assignment 6 - 27 November 2025 
6.	Write a simple guessing game (using while loop) asking the user to input a number.
Let the already fixed number is 7. the program should keep asking the user to inut a number  between 1 to 10.
when user inputs 7, the program should stop asking more guess atempts'''


import random
num=random.randint(1,10)
print("I have selected a number (1 to 10) can you guess it ?   ")

while True:
    guess=int(input("Enter your guess:   "))


    
    if guess == num :
        print("Congratulations! you guessed the Number!",num)
        break




    #if number is less than a selected Number:
    
    elif guess < num:
        print("It's too low! Try again!  ", num)



    #if number is greater than guessed number!
        
    else:
        print("It's too high! Try again! ")

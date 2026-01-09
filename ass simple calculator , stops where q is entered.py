'''
Assignment 4
	Write a python code to Create a simple calculator that asks user to enter 2 numbers and an operator / operation keyword based on
	the user’s choice of operation. - The calculator should keep asking for new operations until the user decides to quit by entering 'q'.
	
	'''

#defining functions 

def add(num1,num2):  #addition
    print(f"The Addition is:  {num1+num2}")



def sub(num1,num2):  #subtraction
    print(f"The Subtraction is:  {num1-num2}")
    



def div(num1,num2):  #division
    print(f"The division is: {num1/num2}")





def mult(num1,num2):  #multiplication
    print(f"The multiplication is :  {num1*num2}")

    


def mod(num1,num2): #modules 
    print(f"The modules is:  {num1%num2}")







while True :

    #accesing values for arguments
    a=input(f"Enter a value , or Enter 'q' to quit:  ").casefold()

                     #checking condition if user entered q
    if a == 'q' :
        break

    

    operator=input(f"choose operation (+,-,/,*,%) or Enter q to quit:   ").casefold()
    if operator == 'q' :   #if user entered q it will stop
        break
    

    b=input(f"Enter second value, or Enter 'q' to quit:  ").casefold()
    if b == 'q' :
        break



    #Program will perform task according to operator 

    if operator == '+' :
        add(float(a),float(b))
        print('-'*50)

    elif operator == '-' :
        sub(float(a),float(b))
        print("-"*50)


    elif operator == '*' :
        mult(float(a),float(b))
        print("-"*50)

    elif operator == '/' :
       div(float(a),float(b))
       print("-"*50)


    elif operator == '%' :
        mod(float(a),float(b))
        print('-'*50)



    else:
       print("Invalid  OPERATION!")











       


















    

    




    
    

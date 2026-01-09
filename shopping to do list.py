#Assignment 1 (9 December 2025)

  #● **Shopping List Application**     
#Write a Python program to create a shopping list. The program should allow the user to:
'''1. Add items to the list.
2. Remove items from the list.
3. View all items in the list.
4. Exit
          options  add item, '''




#creating an empty list to store items


l=[]  
while True:

    #getting choice
    choice=input(('''OPTIONS \n 1- ADD ITEMS: \n 2- REMOVE ITEMS: \n 3-VIEW ADDED ITEMS: \n 4-Exit \n ENTER YOUR CHOICE:  '''))
    print("_"*40)
   


    #CHECKING CHOICE

    if choice== "1" :
        item=input("Enter your item to add:    ")
        l.append(item)
        #what added
        print(f"dear! your added item is {item}.")
        print("-"*40)#print line for easy readability


    elif choice == "2" :
        item=input("Enter item Name you wanna remove:  ")
        
        #lista=[1,2,3,4]
        #itemno = int(input("Enter the task no"))  #for understanding by sir
        #lista.remove((lista[itemno]))
        #print(lista)
        

        #checking if given item is present 
        if item in l:
            l.remove(item)
            #printing what item has removed
            print(f"removed item :  {item}")

        #if item not present in list
        else:
            print(f"dear! item that you entered to remove is not present in you list!")


    #elif choice is 3
    elif choice == '3' :
        if l:
            print("here is , Your shopping list !")
            for indx,item in enumerate(l,start=1):
                print(f"------------------\n {indx } : {item}")
            print("_"*40) #printing  line for easy readabiluty    

                

        else:
            print("your shopping list is empty, dear! ")


    #if choice is 4
    elif choice== '4' :
        exit()


    #if chice in not between choice options

    else:
        print("Invalid choice!")
            









            


            
            
        
        
    

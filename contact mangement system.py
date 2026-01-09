#contact management updated

'''Mini project- 17 December 2025 

Mini project:

Contact Management System with Updates and Error Handling
Write a Python program that uses functions to add, delete, and search for contacts in a dictionary. Each contact should have a name, phone number, and email address. Update the Contact Management System  by:
- Add error handling for duplicate contact names.
- Allow the user to update an existing contact's phone number and email address.
Ghulam Murtaza Channa
•
Dec 17
'''




contacts={}


def add_contact():
    while True:

        print("-----------------------------------------------------------------------")

        name=input("Enter Name:  ").strip()
        phone=input("Enter Phone Number: ").strip()
        email=input("Enter email: ").strip()


        contacts[name]={"name": name , "phone" : phone, "email" : email}

        add_more=input("do you want to add more contacts (y/n): ").strip()

        add_more=add_more.lower()
        if add_more == "y":
            add_contact()  #calling add_contact()  method
            

        else:
            print("exiting...!")
        print("-----------------------------------------------------------------------")
        break




            
def view_contact():
    '''-----------------checking contacts in contacts--------'''
    print("-----------------------------------------------------------------------")
    if not contacts:
        print("No contact found!")
        return

    #while True:

    print("--------------------Total contacts------------------------------")

    for name,info in contacts.items():
        print(f"Name: {name} \nPhone: {info["phone"]} \nEmail: {info["email"]} \n")

    print("-----------------------------------------------------------------------")


    '''view_again=input("do you want to view again (y/n): ").strip()

    view_again=view_again.lower()

    if view_again =="y":
    view_contact()  
        

    else:
    print("exiting...")
    print("-------------------------------------------------------------")'''
    #break
                


            


def remove_contact():

    print("-------------------------------------------------------------")
    if not contacts:
        print("No contact found!")   #if no contacts in contacts
        return

    while True:
        removed_name=input(f"Enter name to remove (or 'q' to quit):  ").strip()
        removed_name=removed_name.lower()
        #removed_name=removed_name.lower()

        if removed_name =="q":   #if user inters q 
            print(f"exiting remove name!")
            break
            

        if removed_name not in contacts: #if given name to remove doesnt exist!
            print(f"{removed_name} doesn't exist!")

            
            print("Try again!")

            continue

            

        else:
            removed_name=contacts.pop(removed_name)  #removing name

            print(f"{removed_name} removed successfully!")


        remove_more=input("Do you want to remove more contacts (y/n): ").strip()

        remove_more=remove_more.lower()

        if remove_more!="y":
            print("exiting...")
            print("-------------------------------------------------------------")
            break
        print("------------------------------------------------------------------------------------")



        
            
        
    

    

            

        
            


def search_contact():
   
    print("------------------------------------------------------------------------------------")
    if not contacts:
        print("no contact found|!")
        return

    while True:
        name=input("Enter name to search: ").strip()

        if name not in contacts:
            print(f"{name} does not exists!")



        elif name in contacts:
            info=contacts[name]

            print(f"Name: {info["name"]}")
            print(f"Phone : {info["phone"]}")
            print(f"Email: {info["email"]}")

            
        '''--------------------asking again for searching contact----------------------------------'''

        search_again=input("Do you want to search again (y/n): ").strip()
        search_again=search_again.lower()

        if search_again !="y":
            print("exiting...")  #-----------exiting
            print("------------------------------------------------------------------------------------")
            break


    print("------------------------------------------------------------------------------------")

         
            
        
    
    


def update_contact():
    

    while True:
        print("----------------------------------------------------------")
        if not contacts:
            print("no contact to update!")
            break

    
        key_name=input("Find Name to update: or (press q to skip)").strip()
        
        key_name=key_name.lower()
        print()

        if key_name=="q":
            print("exiting....")
            break

        if key_name not in contacts:
            print(f"{key_name} not found!")

            continue

   
        name=input("enter name to update or (press enter to skip): ").strip()
        phone=input("Enter phone to update or (press enter to skip): ").strip()
        email=input("Enter email to update or (press enter to skip): ").strip()

        if name:
            contacts[key_name]["name"] = name
        if phone:
            contacts[key_name]["phone"]=phone
        if email:
            contacts[key_name]["email"]=email

        print(f"{key_name} updated successfully!")


        update_more=input("Do you want to update more(y/n): ").strip().lower()
        if update_more!="y":
            print("exiting...")
            break

        print("----------------------------------------------------------")
            
            
        

    

while True:
    try:
        choice=int(input('''1-Add Contacts
2-View Contacts
3-Remove Contacts
4-Search Contacts
5-Update Contacts
6-Exit                     
                     
Enter number (1/6): '''))

        
        if choice==1:
            add_contact()

        elif choice==2:
            view_contact()
            

        elif choice==3:
            remove_contact()

        elif choice==4:
            search_contact()

        elif choice==5:
            update_contact()

        

        elif choice==6:
            print("exiting...")
            exit()
            #exiting=input("do you want exit(y/n)").strip()

        else:
            print("wrong input")
            print("choose only (1/6): ")
            

    except ValueError:
        print("ValueError!")
    










    
        

#TO DO App
#let user mark task as done
#let user remove or delete entire list

to_do_list=[]

while True:

    print('''---Options----
    1-Add Task
    2-View Task
    3-Mark Task as Done
    4-Remove Task or Delete Entire list
    5-exit...''')
    
    try:
        option=input("choose your option:  ").strip()
        
    except: #if wrong input is given
        print(f"wrong option selected: {option} ")
    #menu() #calling menu function


    def add_task():
        
        task=input("Enter your Task to add: ") #accessing task from user

        #appending to_do_list
        to_do_list.append({"task" : task, "status": "pending"})

        print(f"{task} added succesfully!") #message on console ,task added successfully 


    def view_task():
        if len(to_do_list)==0:  #if o item in list
            print("No task to view!")

        else:
            print("--------Total Tasks--------")
            for index,tasks in enumerate(to_do_list, start=1):
                print(f"{index} :{tasks["task"]} - {tasks["status"]}")


    def mark_task_done():
        if len(to_do_list)==0:
            print("No task to mark!")

        else:
            mark_done_input=int(input("Enter number you wanna mark:  "))-1

            if 0<=mark_done_input < len(to_do_list):
                to_do_list[mark_done_input]["status"]="done"   #marking status as done at given index/input number by user

                #printing after marking done
                print(f"{to_do_list[mark_done_input]["task"]} has been marked as done")


            #else
            else:
                print(f"Invalid Input {mark_done_input}")

    def remove_task():
        if len(to_do_list)==0:   #if list is empty
            print("No task in the list!")
            

            '''------------------variable name--------------------------'''
            #delete_list == variable name asking for deleting list or removing task number if done
            #remove_input == variable name for asking the index number of a task , user wannts remove
            

        else:
            try:
                
                delete_list=input("Are you removing marked task or deleting entire list?  (t/l)").strip()#asking for deleting list or task
            #if wrong input give
            except:
                print(f"Wrong input  option : {delete_list}")


            #if user wannts removing  marked task
            if delete_list=="t":
                try:
                            
                    remove_input=int(input("Enter Task Number you wanna remove:  "))-1
               
                    
                            
                    #remove if task in done/completed
                    if to_do_list[remove_input]["status"]=="done":
                                
                        removed_task=to_do_list.pop(remove_input) #removing task number
                        print(f"{removed_task["task"]}: has been removed!")

                    else:
                        print(f"{to_do_list[remove_input]["task"]}: not marked yet , so you cant delete it now!")

                            

                except:  #if wrong charactet input or wrong data type is given 
                    print(f"task number error !")



                '''-----------------------------------------------------------------------------------------------------------'''    
            #if user wanna delete list

            elif delete_list =="l":
                if len(to_do_list)==0:    #if no task (item) in list.
                    print("No Task!")

                
                elif len(to_do_list) >0 :
                    to_do_list.clear()  #deleting to do list

                    print("to do list has been deleted successfully!")
                   
                    




    #calling function()
    if option=="1":
        add_task()

        
    elif option=="2":
        view_task()


        
    elif option=="3":
        mark_task_done()


    elif option =="4":
        remove_task()


    elif option =="5":
        exit()


    else:
        print("Invalid Option!")




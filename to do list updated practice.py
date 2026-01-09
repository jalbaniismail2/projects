#to do list

to_do_list=[] #list to store data

while True:
option=int(input('''-----OPTIONS------\n1-Add Task \n2-View Task\n3-Mark Task as Done\n4-Remove Marked Task \n5-delete entire tasks\n6-Exit App
Choose your option:  '''))


#adding task

def add_task():
    task=input("Enter your task to add: ").strip()
to_do_list.append({'task': task, 'status':'pending'})

print(f"task has been added successfully:     ")





if option=="1":
    add_task()


elif option=="2":
    view_task()


elif option=="3":
    mark_task()


elif option=="4":
    remove_task()


elif option=="5":
    delete_list()


elif option=="6":
    print("Exiting...")
    exit()



else:
    print("Invalid Option!")
    

    

                 




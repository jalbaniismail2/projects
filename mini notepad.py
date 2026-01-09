#mini notepad

#lst=["mexi","ahmed","khan","rahman","sultan","ali"]

import os

while True:
    
    option=input('''\n1-Add File
2-read File
3-Delete File
4-exit

Enter Your Option:  
    ''').strip()



    #add file
    if option=="1":
        filename=input("create file name:       ")
        content=input("add content:  ").strip()
        
        with open(filename,"a")as file:
            file.write(content+"\n")

        print("file added successfully!")   
        


    #view file / read file
    elif option=="2":
        filename=input("search file name:   ").strip() #searching file name
        if os.path.exists(filename):
            with open(filename,"r")as file:

                #file content
                print("----------file content--------------")
                print(file.read())

        else:
            print("FileNotFound !")




            
        '''-------------------------------------------------------'''    

    #delete file from systes
    elif option=="3":
        filename=input("Enter file name:   ").strip()

        
        if os.path.exists(filename):
                print("removing........")
                os.remove(filename)   #removing file
                print("file removed from system!")
                
        
        else:
            print("File not found!  ")


        '''-----------------------------------------------------------'''     
    elif option=="4":
        
        exit()    


    else:
        print("Wrong Input!")

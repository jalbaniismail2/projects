'''''''''''''HOTEL ORDERING SYSTEM---------------------------------'''




'''-------------menu-------------'''
fast_food={"burger":50, "pizza":300, "fries":200}
chinese={"chinese_rice":200, "chinese_food":100, "chinese_meal":400}
bbq={"pasta":400}


add_ons={"extra chees":50, "drink":60}  #add_ons



'''---------------category_option()   created to mention menu category-------------------------'''

def category_option():
    print("---Item Menu-----")
    print("1-Fast Food")
    print("2-Chinese")
    print("3-BBQ")
    print("4-Exit")



grand_total=0  #to calculate total



order_summary={}   #for order summary at end of order








while True:
    category_option()    #calling category method
    
    category=input("Select your category (1/4):  ").strip() #asking for category

    print("------------------------------------")

    
    if category=="1":          #----------------------------category 1--------------fast_food ------------------
        

        order_summary["food_category"]="Fast Food"   #''-----assigning value Fast Food to food category-------'''
        for index,(name,price) in enumerate(fast_food.items(), start=1):
            print(f"{index} - {name} : {price}")
        print("4-exit") #-------exiting

        '''-----------------------------item number-------------------------'''    
        while True:    #keeps asking item number for category 1(fast food ) until the user slects valid item number
            
            try:
                item=int(input("Enter Item Number: (1/4) ")) #accesing item number

                if item==1:
                    order_summary["item"]="burger" #assigning value burger to key item
                    order_summary["price"]=fast_food["burger"]  #burger price to order summary
                    break
                
                elif item==2:
                    order_summary["item"]="pizza"  #name of item to order summary
                    order_summary["price"]=fast_food["pizza"]   #pizza price  to order summary
                    break

                elif item==3:
                    order_summary["item"]="fries"    #item fries assiging to key named item
                    order_summary["price"]=fast_food["fries"]     #fries price to order summary   ,  assigning fries to key named item
                    break

                elif item==4:
                    print("exiting...")
                    exit() #calling exit method


                else:
                    print("wrong input!   ")      #message if wrong category option selected

                                    
            except ValueError:
                print("Please select valid item number!")  #'generating value error message if wrong type value is given by the user

            except Exception as e:
                print("FAST FOOD:  ",e)   #generating exception  (common error generator)











        print("-----------------------------------------------------------------------------")
        '''----------------------------quantity-------fast-food------------------------'''
        while True:
            try:
                    
                quantity=int(input("Enter quantity for the item: ")) #asking quantity
                

                
                    
                if quantity<=0: #if quantity is less than 1
                    print("please Enter gtreater than 0 for quantity!")

                    

                else:
                    order_summary["quantity"]=quantity    #assigning quantity to the key named "quantity" in order_summary
                    order_summary["subtotal"]=order_summary["price"] * order_summary["quantity"]  #counting subtotal

                    #order_summary["subtotal"]=subtotal     #assigning subtotal value to 
                    break #stoping program to ask again if user enters valid quantity value 
                    

            except ValueError:
                print("Please enter numeric quantity value!")
            except Exception as e:
                print("quantity error!",e)













        print("------------------------------------------------------------------------------")
        '''---------------------add-ons----------------------fast-food-------------------------------'''
        while True:
            add_on=input("Do you want add-ons (y/n)  or (q to quit)").strip()  #prompting confirmation message for user
            add_on=add_on.casefold()

            
            if add_on=="q":
                print("exiting...") #exiting.....
                exit()
            elif add_on=="y":  #if user wants add_ons
                for index,(name,price) in enumerate(add_ons.items(), start=1):
                    print(f"{index} - {name} : {price}")  #showing menu for add-ons

                try:
                    print(f"3 - both : {add_ons["extra chees"] + add_ons["drink"]}")
                    print(f"4- exit") #-------------------------------exiting-----------------------------
                    choise=int(input("Choose 3 for both or any one (1/4) :   "))  #offering for both add_ons along with single add-on
                    

                    if choise==3: #3 for both add_ons
                        order_summary["add_on"]="extra chees"  + "drink"   #assigning item names value to the key named "add_ons"  in order_summary
                        order_summary["add_cost"]=add_ons["extra chees"]+add_ons["drink"]  #price for both extra chees and drink


                        '''----------------------------------------------------------------------------order summary--------------------------'''

                        print("----------------order summary---------------------")

                        for name,value in order_summary.items():  #looping for accessing order summary from (order_summary)
                            print(f"{name} : {value}")


                        '''-------------------------------------------grand total---------------------------'''
                        print("---------------------------------------------------")

                        grand_total=order_summary["subtotal"] + order_summary["add_cost"]

                        print("Grand Total: ", grand_total)

                        print("-------------------------------------------------------------------------------")



                        break    #breaking loop to stop



                        #break    #stoping for add_ons  offer after adding price for both items into "add_cost" variable


                    elif choise==1:
                        order_summary["add_on"]="extra chees"  #added item
                        order_summary["add_cost"]=add_ons["extra chees"]  #extra chees price

                        '''--------------------------grand total-------------------------------'''

                        grand_total=order_summary["subtotal"] + order_summary["add_cost"]


                        print("-------------------------------------------------------------------------------------------------")
                        '''--------------------------------------------------------------order summary-----------------'''
                        print("-----------Order Summary--------------")
                        

                        for name,value in order_summary.items():
                            print(f"{name}  : {value}")


                        print("-----------------------------------------------------------")

                        

                        print("grand total:  ",grand_total)  #grand total

                        print("------------------------------------------------------------")   #simple new line for readability

                        break      #'''--------------------------------------breaking after adding cost for extra chees----------------'''


                    elif choise==2:
                        order_summary["add_on"]="drink"   #added item
                        order_summary["add_cost"]=add_ons["drink"]  #drink price


                        '''-----------------------finding grand total----------------------------'''
                        grand_total=order_summary["subtotal"] + order_summary["add_cost"]

                        

                        '''----------------------------------------------------------order summary---------------------------------------------'''
                        print("-----------Order Summary--------------")

                        for name,value in order_summary.items():
                            print(f"{name}  : {value}")


                        print("-----------------------------------------------------------")

                        

                        print("grand total:  ",grand_total)  #grand total

                        print("------------------------------------------------------------")   #simple new line for readability

                       
                        break   #braking after adding cost for drink
                        '''----------------------------------------------------------------------------------------------------------------------'''
                    elif choise==4:
                        print("exiting...")
                        exit()  #calling exit()

                    




                except ValueError:
                    print("Enter only (1/3) options for add_on : ")
                except Exception as e:
                    print("add on error ",e)
    
                        
            elif add_on=="n":  #if user doent wannt add ons

                '''----------------finding grand_total------------------------'''
                grand_total=order_summary["subtotal"] 


                print("-"*50)
                print("-------------order summary------------")

                for name,value in order_summary.items():
                    if "add_on" in order_summary:
                        continue

                    print(f"{name} : {value}") 


                print("----------------------------------------------")

                        
                
                print("Grand Total : ",grand_total) #grand total

                break

            


            else:    
                        
                print("invalid add_on options!")

                '''-------------------------------------------------------------'''                        
                        
                    









                '''=========category 2 ====================chinese items=====================================category 2====================chinese====================='''
    elif category=="2":

        order_summary["food_category"]="chinese"   #-----------------------------adding food_category === chinese
        for index,(item,price) in enumerate(chinese.items(), start=1):
            print(f"{index} - {item} : {price}")  #accesing item-name and item-pricess along with  index from chinese menu(dictionary )
        print("4- exit")
        
        while True:
            try:
            
                print("-"*50)
                choice=input("Enter your choice (1/4):  ").strip()  #asking choise for item , item from chinese menu




                
                if choice=="1":
                    '''---------------------------adding name and price to order_summary (dictionary )-----------------------------'''


                    
                    
                    order_summary["item"]="chinese_rice"  #name of item                       '''adding name to summary dictionary
                    order_summary["price"]=chinese["chinese_rice"]   # price of chinese rice   ''' adding price to summary dictionary
                    
                    break
                

                elif choice=="2":
                    order_summary["item"]="chinese_food"  #name  chinese_food
                    order_summary["price"]=chinese["chinese_food"]  #price of chinese food

                    break
                

                elif choice=="3" :
                    order_summary["item"]="chinese_meal" #name of item
                    order_summary["price"]=chinese["chinese_meal"] #price of chinese_meal

                    break

                elif choice=="4":
                    print("exiting...")
                    exit() #----------calling exit()


            
                else:
                    print("please choose only (1-4) for chinese food ! ")
            except Exception as e:           #'''----------------------------------------------------exception----------------------'''
                print("Chinese food : ",e)




        '''------------------------------------Quantity for chinese food--------------------------------------------'''
        while True:
            try:
                print("-"*50)
                quantity=int(input("Enter quantity for chinese item:  "))

                if quantity<=0:
                    print("Please enter greater than 0 for quantity! ")

                else:
                    order_summary["quantity"]=quantity    #assigning quantity to the key, named quantity

                    order_summary["subtotal"]=order_summary["price"] * order_summary["quantity"]  #adding subtotal
                    break #breaking loop

                    

            except ValueError:
                print("(chinese category): please enter numeric and greater than 0 quantity ")

            except Exception as e:
                print("(Chinese category quantity): ",e)



        '''---------------------------------------add ons-----------for chinese food---------------------'''

        while True:
            add_on=input("do you want add_ons (y/n) or (q to quit):  ").strip()
            add_on=add_on.casefold()
            try:
                if add_on=="q":
                    print("exiting...")
                    exit()
                elif add_on=="y":  #if user wants add_ons
                    print("-"*50)
            
                    for index,(item,price) in enumerate(add_ons.items(), start=1):  #looping in add_ons menu dictionary to get (item name and prices for items)
                        print(f"{index} - {item} : {price}")

                    print("3 - both : ",add_ons["extra chees"] + add_ons["drink"])  #jugar , better use for loop     #oo000800989
                    print("4- exit") #---------------exit option
                        


                    choice=input("choose add-on item:   (1-4)") #asking for add on choice

                    if choice=="3":
                        order_summary["add_on"]=add_ons["extra chees"] + add_ons["drink"]  #adding both  add_ons

                        grand_total=order_summary["subtotal"] + order_summary["add_on"]


                        '''-----------------------------------printing order summary-----------------'''
                        
                        print("-"*50)
                        print("-----------------Order Summary-----------------------")

                        for item, price in order_summary.items():

                            print(f"{item} : {price}")

                        '''------------------------grand total----------------------------'''
                        print("-----------------------------")
                        print(f"grand total: ",grand_total)

                        break






                    elif choice=="1":      #add_ons--------------------chinese category-----------------------
                        
                        print("-"*40)
                        '''-------------adding price of extra chees----------------------'''
                        order_summary["add_on"]=add_ons["extra chees"]         #extra chees price to add_on key in (order_summary)

                        
                        '''--------finding grand_total-----------------------'''
                        grand_total=order_summary["subtotal"] + order_summary["add_on"]    #total=subtotal(price*quantity) + add_on_cost


                        '''-----------------------------------order summary----------------------'''
                        print("------------------order summary---------------")

                        for item,price in order_summary.items():
                            print(f"{item} : {price}")


                        '''------------------------printing grand total-------------------------'''
                        print("------------------------------")
                        print("grand total :  ",grand_total)   #total price for order items

                        print("-"*40)
                        
                        

                        break  #to stop executing

                    

                    elif choice=="2":     #add_on = both    ------------add_ons--------------------chinese category---------------
                        '''----------------adding price of add_on (item == drink)'''
                        order_summary["add_on"]=add_ons["drink"]  #price for drink , assigning to the key named "add_on" in order_summary

                        
                        '''------------------finding grand total------------------------'''
                        grand_total=order_summary["subtotal"]+order_summary["add_on"]       #grand total

                        


                        '''-----------------------------------order summary-----------------drink ----------------chinese category-------------'''

                        print("-"*50)
                        
                        print("----------------Order Summary---------------")
                        for item, price in order_summary.items():
                            print(f"{item} : {price} ")    #items from the temporary data (order_summary)

                        print("-----------------------")
                        print("grand_total : ", grand_total)         #printing grand_total value

                        print("-"*50)


                        break #to stop executing

                    elif choice=="4":
                        print("exiting...")
                        exit()    #==============calling exit()

                    else:
                        print("please select valid item: ")
                    
                

                        '''---------------------------------------------if user doesnt want add_ons-----------along with------chinese items----------'''
                elif add_on=="n":

                    grand_total=order_summary["subtotal"]   #grand_total

                    '''---------------------------------------Order Summary-------------------------chinese category---------------'''
                    print("-"*50)
                    print("-----------Order Summary-------------------")

                    for item,price in order_summary.items():
                        if "add_on" in order_summary.items():   #removing added add_on  '''----<<<<<<<<<<<<<<<<<<<<<<<<<<<---<<>>--><-><>><---->>>-->>>>>>>>>>>>>>
                            continue
                        print(f"{item} : {price} ")               #summary deta


                    print("---------------------------------------------------------------")
                    print("grand total : ",grand_total)  #grand total

                    print("-"*50)

                    break  #break to stop the loop while
                    
                        
                    

                else:
                    print("please make valid selection: (y/n)")
            

            except ValueError:
                print("(chineese food) value error!")   #if value error in chinese add_ons

            except Exception as e:
                print("(chinese food ) :",e)    #common exception



















                '''--------------------------------------------------------Category 3--------------------------BBQ------------------------bbq---------'''

    elif category=="3":
        order_summary["food_category"]="BBQ"             #assigning value bbq to food category

        '''=======================================accessing file======================================'''

        for index,(item,price) in enumerate(bbq.items(),  start=1):

            print(f"{index} - {item} : {price}")     #items from the bbq category
        print("2-exit")

            
        while True:
            try:
                choice=input("Enter your choice (1/2) : ").strip()             #'''-----------------------------------------choice for bbq item-----------------'''

                if choice=="1":
                    order_summary["item"]="pasta"  #assigning value to the key item in dictionary name order_summary{}

                    order_summary["price"]=bbq["pasta"]       # '''---------------value for pasta--------------------------'''

                    break

                elif choice=="2":
                    print("exiting...")
                    exit()   #calling exit


                else:
                    print("please choose wisely ! ")
            except ValueError:
                print("(category BBQ) ValueError") #ValueError
            except Exception as e:
                print("(category bbq) ",e)        #common Exception
                


                '''----------------------------quantity for -----------bbq -------category---------------------------quantity--------------------bbq--------------------------'''
        while True:
            try:
                
                quantity=int(input("Enter quantity for the item in category bbq:  "))

                if quantity<=0:
                    print("Please enter greater than 0 for quantity!  ")


                elif quantity >0:
                    order_summary["quantity"]=quantity   #assigning quantity to the key name quantity

                    order_summary["subtotal"] = bbq["pasta"]  * order_summary["quantity"]  #counting subtotal

                    '''-------------------------breaking loop--------------------------------------'''

                    break  #breaking loop


                else:
                   print("please enter valid quantity for item in category bbq! ")


            except ValueError:       #ValueError
                print("(category bbq) ValueError!")

            except Exception as e:
                print("(Category bbq): ",e)   #common exception




                '''----------------------------------------------------------add_ons------------------------------with bbq category--------------'''
        while True:
             add_on=input("Do you want add_ons(y/n) or (q to quit) :  ").strip()
             add_on=add_on.casefold()
             if add_on=="q":
                 print("exiting...")
                 exit() #------------------------calling exit()
             elif add_on =="y":    #if user wants add_on

                 try:
                    for index,(item,price) in enumerate(add_ons.items(), start=1):

                         print(f"{index} - {item} : {price}")    #items in      add_ons{}

                    print(f"3 - both : {add_ons["drink"] + add_ons["extra chees"]}")    #option 3 for both (extra chees and drink)
                    print("4- exit") #------------exit option


                    '''----------------------------asking for add_ons choice------------------'''
                     
                    '''-----------------------------------------------add_ons-------for both items-----------category--------bbq-------'''    
                    choice=input("choose add_on item (1-4) : ")
                    
                         
                    if choice=="3":

                        order_summary["add_on"]=add_ons["drink"] + add_ons["extra chees"]  #add_on added
    



                        '''-------------------grand total--------------------------'''
                        grand_total=order_summary["subtotal"] + order_summary["add_on"]



                        '''---------------------------order summary-------------------------------'''
                        print("--------------order summary---------------")

                        for item,price in order_summary.items():

                            print(f"{item} : {price}")



                        print("---------------------------------------")      # '''------------grand_total-------------'''
                        print("grand total : " ,grand_total)

                        print("-"*50)
                        
                        
                 
                        break   #stoping program after printing order summary


                 
                    elif choice =="1":
                        try:
                            
                            order_summary["add_on"]=add_ons["extra chees"] #assigning value to key
                            

                            '''----------------------------grand total-----------------------------'''

                            grand_total=order_summary["subtotal"] + order_summary["add_on"]


                            '''-----------------------------order-summary-------------------'''
                            
                            print("------------------------------------------------------------------")
                            for item,price in order_summary.items():
                                print(f"{item} : {price}")

                            '''-----------------------------------------------grand total-----------------------------'''

                            
                            print("----------------------------------------------------")
                            print(f"grand total: ",grand_total)

                            print("-"*50)

                            
                            break #break
                            
                        except Exception as e:
                            print("(category: bbq ---add_ons--- :  )",e)





                    elif choice =="2":
                        try:
                            
                            order_summary["add_on"]=add_ons["drink"] #assigning value to key
                            

                            '''-----------------------finding-----grand total-----------------------------'''

                            grand_total=order_summary["subtotal"] + order_summary["add_on"]


                            '''-----------------------------order-summary-------------------'''
                            for item,price in order_summary.items():
                                print(f"{item} : {price}")

                            '''-----------------------------------------------grand total-----------------------------'''
                            print("------------------------------------------------")
                            print(f"grand total: ",grand_total)

                            print("-"*50)
                            break #break


                        
                            
                        except Exception as e:
                            print("(category: bbq ---add_ons--- :  )",e)


                    elif choice=="4":
                        print("exiting...")
                        exit() #calling exit()

                 except ValueError:
                     print("(Category bbq): ValueError!")

                 except Exception as e:
                    print("(Category bbq): ",e)


                    
             elif add_on=="n":
                 try:
                                      

                     grand_total=order_summary["subtotal"]   #calculating grand_total

                     
                     '''------------------------order summary------------------------'''
                     print("---------------order summary------------")

                     for item,price in order_summary.items():
                         if "add_on" in order_summary.items():
                             continue

                    
                         print(f"{item} : {price}")


                     '''-----------------------grand total-------------------------------'''
                     print("------------------------------------------------------------")
                     print("grand total : ",grand_total)  #grand total

                     print("-"*50)

                     break


                    

                 except Exception as e:
                     print("(category bbq ) add_on ==n:    ",e)



             else:
                 print("please enter only y/n !")


                 
                    
                
             





                

            
                


            
    elif category=="4":
        print("exiting...")
        exit()
    else:   #message for wrong input choice for  category 
        print("Invalid Category!")

    #break             #yahan par break lagao to summary output ke bad ruk jata he (or agar galat category choice''' karo to break ho jata he loop)
    '''hite question aa break lae'''



'''-----------------------------------hin khe chade dio ---------------------------------'''
'''-----------------------------Grand total-------------------------------------------------'''


#grand_total=order_summary["subtotal"] + order_summary["add_cost"]

#print("grand total:  ",grand_total)





















    

'''--------------smart travel planner------------------'''

print("====================Welcome Smart Travel Planner================================")


bus_fair=50
taxi_fair=100
metro_fair=80

bus_time=["morning", "evening"]
taxi_time=["morning", "afternoon", "evening"]
metro_time=["afternoon", "evening"]

transport=""
travel_time=""

fair=0
total=0
extra_service=0
priority_boarding_price=0


try:
    '''-----------------------asking for city-------------------------------'''
    selected_city=int(input('''==============cities=======================

    1-Islamabd
    2-Lahore
    3-Karachi

    select your city:  
    '''))

    if selected_city ==1:
        city="Islamabad"

    elif selected_city==2:
        city="Lahore"

    elif selected_city==3:
        city="karachi"

    else:
        print("select valid city!")
        exit()



    selected_transport=int(input('''===============transport=============================

1- Bus
2-taxi
3-metro

select transport:  '''))

    try:
        

        if selected_transport==1:       #--------- 1==bus
            
            time=input('''your prefered time:  morning\n afternoon\n evening
    Select your time: ''').strip() #time == variable (for asking time)

            

            if time in bus_time:     #bus_time==list  ---------morning and evening only
                
                try:
                    
                    budget=int(input('''enter your budget:  bus(50): '''))    #------------asking for budget

                    if budget>=bus_fair:    #checking budget for bus service

                        transport="Bus"       #-------transport-------------
                        travel_time=time  #tavel time

                        fair=bus_fair #bus_fair

                    else:
                        print("Insufficient budget!")
                        exit()
                except ValueError:
                    print("bus budget:  enter valid bus budget!")

            else:
                print("bus time is only morning and evening!")
                exit()



                '''--------------------------------------------------------------taxi--------------------------------------------------------'''
        elif selected_transport==2:       #--------- 2==taxi
                
            time=input('''your prefered time:  morning\n afternoon\n evening
        Select your time: ''').strip() #time == variable (for asking time)

                

            if time in taxi_time:     #taxi_time==list  ---------morning , afternoon and evening only
                    
                try:
                        
                    budget=int(input('''enter your budget:  taxi(100): '''))    #------------asking for budget

                    if budget>=taxi_fair:    #checking budget for taxi service

                        transport="taxi"       #-------transport-------------
                        travel_time=time  #tavel time

                        fair=taxi_fair #taxi_fair

                    else:
                        print("Insufficient budget!")
                        exit()
                except ValueError:
                    print("bus budget:  enter valid taxi budget!")

            else:
                print("taxi time is only morning , afternoon and evening!")
                exit()





                '''--------------------------------------------------------------metro--------------------------------------------------------'''
        elif selected_transport==3:       #--------- 3==metro
                
            time=input('''your prefered time: \nmorning, afternoon\n evening
        Select your time: ''').strip() #time == variable (for asking time)

                

            if time in metro_time:     #metro_time==list  --------- afternoon and evening only
                    
                try:
                        
                    budget=int(input('''enter your budget:  metro(80): '''))    #------------asking for budget

                    if budget>=metro_fair:    #checking budget for metro service

                        transport="metro"       #-------transport-------------
                        travel_time=time  #tavel time

                        fair=metro_fair #metro_fair

                    else:
                        print("Insufficient budget!")
                        exit()
                except ValueError:
                    print("metro budget:  enter valid metro budget!")

            else:
                print("metro time is only  afternoon and evening!")
                exit()
        else:
            print("select valid transport !")
            exit()






    except Exception as e:
        print("transport :  ",e)









            

        '''---------------------- extra service-----------------------'''

    optional=input("do you want extra service (y/n)").strip()  #asking for extra service

    if optional=="y":
        choice=int(input('''----------extra service-------------
1-meal (20)
2-guide (30)
3-priority boarding(40)

enter your service: '''))      #------------extra service??


        if choice==1:
            extra_service="meal"
            meal_price=20
            total=bus_fair+meal_price

            print(f'''----------receipt-------------
Transport : {transport}

Travel Time : {travel_time}
Fair : {fair}
Extra service : {extra_service}
Extra Price : {meal_price}
--------------------------------
Total : {total}

thank you for our smart travel planner!''')

        elif choice==2:
            extra_service="guide"
            guide_price=30
            total=bus_fair+guide_price


            print(f'''----------receipt-------------
Transport : {transport}

Travel Time : {travel_time}
Fair : {fair}
Extra service : {extra_service}
Extra Price : {guide_price}
--------------------------------
Total : {total}

thank you for our smart travel planner!''')


                    
        elif choice==3:
            extra_service="priority boarding"
                
            priority_boarding_price=40
            total=bus_fair+priority_boarding_price


            print(f'''----------receipt-------------
Transport : {transport}

Travel Time : {travel_time}
Fair : {fair}
Extra service : {extra_service}
Extra Price : {priority_boarding_price}
--------------------------------
Total : {total}

thank you for our smart travel planner!''')


            


        else:
            print("wrong service!")
            exit()



    elif optional=="n":

        print(f'''----------receipt-------------
Transport : {transport}

Travel Time : {travel_time}
Fair : {fair}
Extra service : {extra_service}
Extra Price : {priority_boarding_price}
--------------------------------
Total : {total+fair}

thank you for our smart travel planner!''')


    else:
        print("please select only  (y/n) !")
        exit()
            






except ValueError:
    print("ValueError")



            

            

                
                    
                
                

            











        
        
        

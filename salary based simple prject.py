'''
Project Description

This project manages an employee’s salary using .

The salary is and .

Salary can only be viewed or increased using .

Class name: 

Employee


 
Variables (Data Members)  
Public Variables

name                (Stores employee name)
emp_id             (Stores employee ID)

 Private Variables
 

__salary          (Stores employee salary (hidden & protected))

Methods / Functions  
__init__()                                     (initialises name, ID, and salary)
get_salary()                                (Returns employee salary)
increment_salary(amount)       (Increases salary by given amount)
display_employee()                   (Displays employee details)


Program Flow (Step-by-Step)



Program starts



User enters:
Employee name
Employee ID
Initial salary


Employee object is created



Menu is displayed:
View employee info
View salary
Increment salary
Exit


User selects an option



The system performs action using methods


Menu repeats until exit

'''



class Employee:

    def __init__(self, name, emp_id, salary):

        self.name=name
        self.emp_id=emp_id
        self.__salary=salary   #__salary is private atribute at self memory location


        print()


    def get_salary(self):   #'''======for accessing  salary(sensitive informations) ---------'''

        return self.__salary    #'''---------returning salary to the method get_salary=========='''

        print()


    def increment_salary(self,amount):  #increment will be in a fixed amount instead of percentage

        
        self.amount=amount

        self.__salary+=amount

        print(f"salary increased : {self.amount}") #increased amount

        print(f"updated salary:  {self.__salary}")

        print()

        

        


    def display_employee(self):    #employee data
        

        print("-------employee info--------------")  #employee information 

        print(f"Name: {self.name}")    #displaying name and employe id

        print(f"Id: {self.emp_id}")


        print()


    


    

while True:
    try:
        name=input("Enter employee name:  ")   #employeee name

        
        emp_id=int(input("Enter employee id :  "))  #employee id


        emp_salary=float(input("Enter employee initial salary:  ")) #employee salary

        print()        


        emp=Employee(name,emp_id, emp_salary)       #created object emp(class Employee)
        '''--------------------------------------------------- emp (object name)
                                                               Employee()  (class name)''' # class name and object name



        #-------------menu---------------- '''---------------------------------menu------------------------------------------'''##
        print("----Menu----")

        choice=input('''1-view employee info
2-view salary
3-increment salary
4-exit

Enter choice only(1-4):  ''')   #asking for choice

        print("-"*40)

                     

        if choice=="1":
            emp.display_employee()   #calling display_employee() method for accessing info for employee

        elif choice=="2":
            print(f" Salary:  {emp.get_salary()}")  #-------- getting salary by calling get_salary()
           

        elif choice=="3":
            increment_amount=float(input(f"Enter increment in rupees:  ")) #accessing increment amount in rupees

            emp.increment_salary(increment_amount)  #adding increament amount to the salary
            

           

        elif choice=="4":

            print("exiting.......")       #exiting / stoping the program
           
            break

        else:
            print("Try again! invalid option!")
            print()


        

    except ValueError as ve:
        print("Value Error: ", ve)
        print()


    except Exception as e:
        print("exception error: ",e)
        print()

        


















        

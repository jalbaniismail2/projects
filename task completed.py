#task completed

l=[]
name=input("Enter task you wanna check if it is done or pending")

dic={"task": name, "status" : "pending"}

l.append(dic)

print(l)

dic["status"] = "done"

print(l,"dic print")
    

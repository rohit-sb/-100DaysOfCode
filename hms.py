#write a function which takes client names as a input. 
def gatedate():
    import datetime
    
    return datetime.datetime.now()
#print("[",gatedate(),"]")
print("Welcome to Gym Hayatt. ")
print("Harry || Hammad || Rohan are our top existing users.\n ")
userType=input("Enter'E' for existing user and 'C' to create new user: ")
if userType.capitalize()=="C":
    name=input("Enter your username: ")
    age=input("Enter your age: ")
    contact=input("Enter you contact:  ")
    newFile=open("newuser.txt","a")
    newFile.write("["+ str(gatedate())+"]"+name+" "+age +" "+contact+"\n")
    print("We will contact you after your account is set up. ")
    quit()
elif userType.capitalize()=="E":
    condition=True
    while condition==True:
        clientName=input("Enter client name: ")
        checker=input("Log or Retrive: ")
        toDo=input("Food or Exercise: ")
        def harryFile():
            '''this function manages activities related to harry'''
            if toDo.lower()=="food":
                if checker.lower()=="log":
                    file1=open("harryfood.txt","a")
                    food=input("Enter the Food: ")
                    file1.write("["+str(gatedate())+"] "+food+"\n")
                    print("Data Entered Sucessfully!")
                elif checker.lower()=="retrive":
                    file1=open("harryfood.txt","r")
                    print(file1.read())
                file1.close()
            elif toDo.lower()=="exercise":
                if checker.lower()=="log":
                    file2=open("harrygym.txt","a")
                    gym=input("Enter the exercise: ")
                    file2.write("["+str(gatedate())+"] "+gym+"\n")
                    print("Data Entered Sucessfully!")
                elif checker.lower()=="retrive":
                    file2=open("harrygym.txt","r")
                    print(file2.read())
                else:
                    print("Wrong Input!")
                file2.close()
        def hammadFile():
            '''this function manages activities related to hammad'''
            if toDo.lower()=="food":
                if checker.lower()=="log":
                    file1=open("hammadfood.txt","a")
                    food=input("Enter the Food: ")
                    file1.write("["+str(gatedate())+"] "+food+"\n")
                    print("Data Entered Sucessfully!")
                elif checker.lower()=="retrive":
                    file1=open("hammadfood.txt","r")
                    print(file1.read())
                else:
                    print("Wrong input")
                file1.close()
            elif toDo.lower()=="exercise":
                if checker.lower()=="log":
                    file2=open("hammadgym.txt","a+")
                    gym=input("Enter the exercise: ")
                    file2.write("["+str(gatedate())+"] "+gym+"\n")
                    print("Data Entered Sucessfully!")
                elif checker.lower()=="lock":
                    file2=open("hammadgym.txt","r")
                    print(file2.read())
                else:
                    print("Wrong input")
                file2.close()
        def rohanFile():
            '''this function manages activities related to rohan'''
            if toDo.lower()=="food":
                if checker.lower()=="log":
                    file1=open("rohanfood.txt","a")
                    food=input("Enter the Food: ")
                    file1.write("["+str(gatedate())+"] "+food+"\n")
                    print("Data Entered Sucessfully!")
                elif checker.lower()=="retrive":
                    file1=open("rohanfood.txt","r")
                    a=file1.read()
                    print(a)
                else:
                    print("Wrong input")
                file1.close()
            elif toDo.lower()=="exercise":
                if checker.lower()=="log":
                    file2=open("rohangym.txt","a+")
                    gym=input("Enter the exercise: ")
                    file2.write("["+str(gatedate())+"] "+gym+"\n")
                    print("Data Entered Sucessfully!")
                elif checker.lower()=="retrive":
                    file2=open("rohangym.txt","r")
                    print(file2.read())
                else:
                    print("Wrong input")
                file2.close()
        if clientName.lower()=="harry":
            harryFile()
        elif clientName.lower()=="hammad":
            hammadFile()
        elif clientName.lower()=="rohan":
            rohanFile()
        else:
            print("Sorry, User is not registered. ")
        looper=input("Press'C' to Continue,'E' to Exit: ")
        print("\n")
        if looper.lower()=="C":
            condition=True
        elif looper.lower()=="e":
            print("Thank You !")
            condition=False
else:
    print("Wrong Input !")
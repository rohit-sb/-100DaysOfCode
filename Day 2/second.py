#Loops
'''
age=int(input("Enter your age: "))
while 10<= age <= 19:
    print("You are teenager", age + 1)
    age+=1
    continue'''
'''sucessful = True
for age in range(1,4):
    print(" Rambas")
    if sucessful:
        print("Rambas delivered")
    else:
        print("Not delivered")
    age+=1
    continue'''
    #make a list and print only numbers which are greater than 6
'''rep=True
while True:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter 2nd number: "))
    opr= int(input("Enter 1 for addition, 2 for Subtraction, 3 for Multiplication and 4 for Division: "))
    sum=num1+num2
    sub=num1-num2
    product=num1*num2
    div=num1/num2
    if num1==45 and num2== 3 and opr==3:
        print("45*3=555")
    elif num1==56 and num2== 9 and opr==1:
        print("56+1=77")
    elif num1==56 and num2== 6 and opr==4:
        print("56/6=4")
    elif opr==1:
        print("Sum of ",num1, " and ", num2,"is" ,sum )
    elif opr==2:
        print("Difference of ",num1, " and ", num2,"is" ,sub )
    elif opr==3:
        print("Product of ",num1, " and ", num2,"is" ,product )
    elif opr==4:
        print("Division of ",num1, " by ", num2,"is" ,div )
    else:
        print("Please enter correctly.")
    for (opr=1):
        if num1==56 and num2== 9:
        print("56+9=577")
        else:
            print(sum)
        break
    for opr=3:
        if num1==45 and num2== 3:
        print("45*3=555")
        else:
            print(product)
        break
    for opr==1:
        if num1==45 and num2== 3 and opr==3:
        print("45*3=555")
        else:
            print(sum)
        break '''
mealcost=float(input("Enter the cost: "))
tip=float(input("Enter the tip percentage: "))
tax=float(input("Enter the tax percentage: "))
tipprice= tip/100 * mealcost
taxprice= tax/100 * mealcost
totalprice = mealcost+tipprice+taxprice
roundedprice= round(totalprice)
print("Total Price is: ", roundedprice)
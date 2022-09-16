#day1
#stringformatting is same as in C language, but it doesn't work for reading input.
'''str_name="rohit"
var_age= 19
print("Your name is %s and you are %d years old" %(str_name, var_age))'''
#ifelse
'''name=input("Your name: \n") 
age=input("Your Age: ")
if int(age)<18:
    print(str(name) + " is not eligible to drive")
else:
    print(str(name) + " is  eligible to drive")'''

#To take a number and check whether the number even or not, and also distinguish its range

num=int(input("Enter a number: "))
result= num % 2
if result != 0:
    print("Weird")
elif result == 0 and 2<= num <= 5:
    print("Not Weird ")
elif result == 0 and 6<= num <= 20:
    print("Weird")
elif result == 0 and num>20:
    print("Not Weird ") 
    
#to print the last digit of the number
'''num=int(input("Enter any number: "))
result=num % 10
print("the last digit is: ",result)'''

#various problems in loops: 
#this 1st problem is based on making a simple guessing game.
'''num=23
turn=0
while True:
    turn=turn+1
    guess=int(input("Enter you guess: "))
    if guess > num:
        print("You guessed high.")
        continue
    elif guess < num:
        print("You guessed low.")
        continue
    if guess == num:
        print("You guessed correct in ", turn, "times")
        break
'''
#2nd problem: Write a program to print the following number pattern using a loop.
'''1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 '''
#Write a program to accept a number from a user and calculate the sum of all numbers 
# from 1 to a given number
'''sum=0
num=int(input("Enter a number: "))
for num in range(0, num+1):
    sum=sum+(num)
    num-=num
    continue
print(sum)'''
#lists
'''
age=[23,25,34,67]
age.append(34)
del(2)
print(age)'''
#taking a number and printing its reverse order 
"""num=int(input("Enter a number: "))
sum=""
while True:
    result=num%10
    sum=sum+str(result)
    num=num//10
    if num==0:
        break
print("The reverse order is: ", sum) """
#FUNCTIONS IN PYTHON
'''def fun():
    num=input("Enter")
    print("this is a function.")
    print(num)
    return
fun()'''
print("Enter 2 numbers.")
c=float(input())
d=float(input())
def function1(a,b):
    average=(a+b)/2
    #print(average)
    return average
v= function1(c,d)
print(v)
# nestList=['a',['b','c',[3,4],'f'],28]
# print(nestList)
#  print(nestList[1])
#  print(nestList[1][2])
# print(nestList[1][2][1])
# nestList.extend([14,78])
# print(nestList)
import random
while True:
    number=random.randrange(1,20)
    print("Guessing Game!\nThe Number is between 0 and 20")
    n=5
    chanceTaken=0
    while chanceTaken < n:
        userChoice=int(input("Enter your choice: "))
        chanceTaken=chanceTaken+1
        if userChoice== number:
            print("Your guess is correct!")
            print("You guessed in ", chanceTaken, "tries. \n ")
            break
        elif userChoice != number:
            print("Your guess is not correct")
            if userChoice>number:
                print("You guessed High.")
            else:
                print("You guessed low.")
            print("You have", (n-chanceTaken),"remaining Life.\n")
            continue
    if chanceTaken==5:
        print("You ran out of Life.")
    looper=input("Enter 'C' to play again and 'E' to exit: ")
    if looper.lower()=='c':
        continue
    elif looper.lower()=='e':
        print("Thank you for playing.")
        break
    else:
        print("Wrong input")
        quit()
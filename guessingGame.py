#this version is a bit faulty
import random
while True:
    number=random.randrange(1,25)
    print("Guessing Game!\nThe Number is between 0 and 25")
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
    if chanceTaken>5:
        #this if condition is faulty
        print("You ran out of Life.")
        print("The number was: ",number,"\n")
    looper=input("Enter 'C' to play again and 'E' to exit: ")
    if looper.lower()=='c':
        continue
    elif looper.lower()=='e':
        print("Thank you for playing.")
        break
    else:
        print("Wrong input")
        quit()

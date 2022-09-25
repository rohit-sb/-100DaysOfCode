import random
while True:
    number=random.randrange(0,25)
    print("\nGuessing Game!\nThe Number is between 0 and 25\n")
    n=5
    chanceTaken=0
    chancesLeft=5

    while chanceTaken < n:
        userChoice=int(input("Enter your choice: "))
        chanceTaken=chanceTaken+1
        chancesLeft=(n-chanceTaken)
        if userChoice== number:
            #correct answer
            print("Your guess is correct!")
            print("You guessed in ", chanceTaken, "tries. \n ")
            break
        elif userChoice != number:
            #incorrect answer
            print("Your guess is not correct")
            if userChoice>number:
                print("You guessed High.")
            else:
                print("You guessed low.")
            if chancesLeft!=0:
                print("You have", (chancesLeft),"remaining Life.\n")
            #user lost the game and displaying out
            elif chancesLeft==0:
                print("You ran out of Life.")
                print("The number was: ",number,"\n")
            continue
    looper=input("Enter 'C' to play again and 'E' to exit: ")
    if looper.lower()=='c':
        continue
    elif looper.lower()=='e':
        print("Thank you for playing.")
        break
    else:
        print("Wrong input")
        quit()

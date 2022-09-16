import random
options=["Rock","Paper","Scissor"]
print("ROCK - PAPER - SCISSOR!")
print("Hi, I'm Computer. I challange you to play with me.")
print("Win: 2 Points & Draw: 1 Point. \n")
while True:
    compPoint=0
    userPoint=0
    for i in range(5):
        compChoice= random.choice(options)
        userChoice=input("Enter your choice: ")
        def rock():
            global compPoint
            global userPoint
            if userChoice.lower()=='rock':
                print("Draw\n")
                userPoint =userPoint+1
                compPoint=compPoint+1
            elif userChoice.lower()=='paper':
                print("You Win\n")
                userPoint =userPoint+2
            elif userChoice.lower()=="scissor":
                print("I Win\n")
                compPoint=compPoint+2
            else:
                print("Wrong Input. Try Again!\n")
        def paper():
            global compPoint
            global userPoint
            if userChoice.lower()=='paper':
                print("Draw\n")
                userPoint =userPoint+1
                compPoint=compPoint+1
            elif userChoice.lower()=='scissor':
                print("You Win\n")
                userPoint =userPoint+2
            elif userChoice.lower()=="rock":
                print("I Win\n")
                compPoint=compPoint+2
            else:
                print("Wrong Input. Try Again!\n")
        def scissor():
            global compPoint
            global userPoint
            if userChoice.lower()=='scissor':
                print("Draw\n")
                userPoint =userPoint+1
                compPoint=compPoint+1
            elif userChoice.lower()=='rock':
                print("You Win\n")
                userPoint =userPoint+2
            elif userChoice.lower()=="paper":
                print("I win\n")
                compPoint=compPoint+2
            else:
                print("Wrong Input. Try Again!\n")
        if compChoice.lower()=='rock':
            print("My Choice: ", compChoice)
            rock()
        elif compChoice.lower()=='scissor':
            print("My Choice: ", compChoice)
            scissor()
        elif compChoice.lower()=='paper':
            print("My Choice: ", compChoice)
            paper()
    print("My Points: ", compPoint,"Your Points: ", userPoint)
    if compPoint > userPoint:
        print("I WIN! YOU CAN NOT DEFEAT ME.\n")
    elif userPoint > compPoint:
        print("YOU WIN! I ACCEPT MY DEFEAT.\n")
    else:
        print("IT IS A DRAW\n")
    print("Do you want to play again?")
    rematch=input("Enter 'C' to play again and 'E' to exit.")
    if rematch.lower()=="c":
        print("\n It's a Rematch. \n")
        continue
    elif rematch.lower()=="e":
        print("\nIt was good to play with You. <333\n")
        break
    else:
        print("wrong input\n")
        quit()
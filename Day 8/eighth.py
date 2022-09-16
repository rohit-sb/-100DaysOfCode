# file=open("checker.txt","a")
# while True: 
#     userId=input("Enter the Id number: \n")
#     if userId =='5113':
#         print("This is rohit.\n")
#     elif userId == '5114':
#         print("This is nisha.\n")
#     elif userId == '5115':
#         print("This is Ritu.\n")
#     else:
#         print("Please enter correctly.")
#     file.write(userId+"\n")
#     checker=int(input("Enter 1 to continue 0 to exit 2 for admin: "))
#     if checker==1:
#         continue
#     elif checker ==0:
#         break
#     elif checker ==2:
#         file=open("checker.txt","r")
#         print(file.read())
#         break
# file.close()

# you need to use information like the number of bedrooms and bathrooms to predict the price of a house.
# Inspired by this competition, you'll write your own function to do this.
# userBeds=int(input("Enter num. of beds: \n"))
# userBaths=int(input("Enter num. of baths: \n"))
# def get_expected_cost(beds, baths):
#     value=80000
#     for num in range(beds+1):
#         for num2 in range(baths+1):
#             value1=value+(10000*num2)
#         value2=value1+(30000*num)
#     return value2
# #print(get_expected_cost(userBeds,userBaths))
# """ IF USER WANTS TO CHECK POSSIBLE COST OF VARIOUS OPTIONS"""
# print("Option A= 2 Bedroom and 3 Bathrooms.\nOption B= 3 Bedroom and 2 Bathrooms.")
# print("Option C= 3 Bedroom and 3 Bathrooms.\nOption D= 3 Bedroom and 4 Bathrooms.\n")
# userOption=input()
# if userOption=="A" or "a":
#     print("Expected Price: ", get_expected_cost(2,3))
# elif userOption=="B" or "b":
#     print("Expected Price: ", get_expected_cost(3,2))
# elif userOption=="C" or "c":
#     print("Expected Price: ", get_expected_cost(3,3))
# elif userOption=="D" or "d":
#     print("Expected Price: ", get_expected_cost(3,4))
# else:
#     print("Enter correctly.")
#to input a list of scores, and print the runner up
numOfdata = int(input("Enter num of data: "))
scores=[]
# for num in range(numOfdata):
#     score = int(input("Score: "))
#     scores.append(score)
scores = list(map(int, input("Enter multiple values: ").split())) #it takes all the elemetns as input at once
winner=scores[0]
runnerUp=-100
for marks in scores:
    if marks> winner:
        winner=marks
    for runnerMarks in scores:
        if runnerMarks>runnerUp and runnerMarks < winner:
            runnerUp=runnerMarks
print(runnerUp)



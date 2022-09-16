#"a" mode is used to append something to the file
# f=open("rohit.txt", "a")
# f.write("Rohit sind gut jung.\n")
# f.close()

#"r" mode is used to read content in a file
# f=open("rohit.txt", "r")
# print(f.read())
# f.close()

#"w" is used to write content in a file, but everytime you run it through, it replaces the content
# f=open("rohit.txt","r")
# f.write("This is america")
# f.close()

# #"r+" mode is used for both, reading and writing
# f=open("rohit.txt","r+")
# a=f.read()
# print(a,"\n")
# f.write("New content\n")
# f.close()

n=int(input("Enter the row: "))
Bool=int(input("Enter 1 or 0: "))
def forBool():
    False
    if Bool == 1:
        return True
    elif Bool == 0:
        return False
    else:
        print('Enter correctly !')
a= forBool()
if a == True: 
    for row in range(n+1):
        print("*"*row)
        n+=n
elif a ==False:  
    for row in range (n+1):
        print("*"*n)
        n=n-1
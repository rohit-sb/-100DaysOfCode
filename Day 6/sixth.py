'''
    looper= "c"
while True:
    userNum=int(input("Enter a number: "))
    def factorial(num):
        answer=0
        while num>=1:
            answer = num*(num-1)
            num-=num
            continue
        return answer

    print("Factorial is:", factorial(userNum))
    looper=input("Enter 'C' to continue: ")
    if looper != 'c':
        break
    else:
        continue
    '''
#ls=[i for in in range(100)]
#print(ls)
# print([[x,y] for x in [2,3,4,5] for y in [3,'g',5,9]])
'''i=int(input())
j=int(input())
k=int(input())
n=int(input())
toBe= [[x,z,y] for x in i for y in j for z in y if x+y+z!=n]
'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    first_list = [x for x in range(x + 1)]
    second_list = [y for y in range(y + 1)]
    third_list = [z for z in range(z + 1)]
    result_list = [[i, j, k] for i in first_list 
                                for j in second_list
                                    for k in third_list
                                        if sum([i, j, k]) != n]
    print(result_list)
# list1=[]
# for r in range(10):
#     z= 3*(r+1)
#     list1.append(z)
# print(list1)
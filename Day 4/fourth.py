'''
userYear=int(input("Enter the year: "))
def year_check(year):
    leap=False
    byFour=year%4
    if byFour == 0:
        byHundred=year%100
        byFourHun=year%400
        while byHundred==0 and byFourHun==0:
            leap=True
            print(year, "is a leap year")
            break
        while byHundred ==0 and byFourHun !=0:
            leap=False
            print(year, "is a leap year")
            break
    else:
        print(year, " is not leap year.")
    return leap
checkYear=year_check(userYear)
print(checkYear)
'''
'''def is_leap(year):
    leap = False
    byFour=year%4
    if byFour==0:
        by100=byFour%100
        while by100==0:
            by400=byFour%100
            while by400==0:
                leap=True
                print("leap")
                break
            break
    
    else:
        leap=False
        print("Not leap")
    # Write your logic here
    print("not leap")
    return leap

year = int(input())
print(is_leap(year))
'''
def is_leap(year):
    """This is a function to check the Leap Year."""
    #comment written in firstline like above is called a doctstring, and it is used to define
    #or state the application of the function.
    leap = False
    byFour=year%4
    if byFour==0:
        by100=year%100
        by400=year%400
        if by100 ==0 and by400==0:
            leap=True
        elif by100 ==0 and by400!=0:
            leap=False
        elif by100!=0:
            leap=True
    else:
        leap = False
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))
print(is_leap.__doc__)

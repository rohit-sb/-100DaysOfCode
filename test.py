n = int(input())
student = []
for i in range(n):
    nameGrade = []
    name = input()
    marks = float(input())
    nameGrade.append(name)
    nameGrade.append(marks)
    student.append(nameGrade)


def topStudent():
    global lowestGrade
    lowestGrade = 101
    for i in range(n):
        grade = student[i][1]
        if grade < lowestGrade:
            lowestGrade = grade
    return lowestGrade


def runnerUp():
    global secondStudent
    topStudent()
    secondGrade = 100
    secondStudent = []
    for i in range(n):
        grade = student[i][1]
        if grade <= secondGrade and grade > lowestGrade:
            second = student[i][0]
            secondStudent.append(second)
            secondGrade = grade
    return secondStudent
runnerUp()
secondStudent.sort()
length=len(secondStudent)
for i in range(length):
    print(secondStudent[i])

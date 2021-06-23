
gradeArray=[]                                                                       # Najprej moreš narediti array
gradeArray.append(5.5)
gradeArray.append(3.2)                                                              # Potrebno je določiti vrednost
gradeArray.append(-2.7)

gradeArray[1]=255.5                                                                 # Če array vsebuje vrednost na [1] mu lahko spremenimo vrednost


print(gradeArray)
print(gradeArray[1])

gradeArray=[]
numGrades=int(input("How many Grades Do You Have? "))

for i in range (0,numGrades,1):
    grade=float(input("Input the grade: "))
    gradeArray.append(grade)

for i in range (0,numGrades,1):
    print("Your ",i+1," grade is ",gradeArray[i])


print("Thats all folks")
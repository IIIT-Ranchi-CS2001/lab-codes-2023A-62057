Name=str(input("Enter name : "))
RollNumber=int(input("Enter Roll Number : "))
Marks=int(input("Enter marks : "))

if (Marks>=90):
    print("Name : ",Name)
    print("Roll No : ",RollNumber)
    print("Grade point : 10")
    print("Remarks : Outstanding")
elif (Marks>=80 and Marks<90):
    print("Name : ",Name)
    print("Roll No : ",RollNumber)
    print("Grade point : 9")
    print("Remarks : Very good")
elif (Marks>=70 and Marks<80):
    print("Name : ",Name)
    print("Roll No : ",RollNumber)
    print("Grade point : 8")
    print("Remarks : Good")
elif (Marks>=60 and Marks<70):
    print("Name : ",Name)
    print("Roll No : ",RollNumber)
    print("Grade point : 7")
    print("Remarks : Average")
elif (Marks>=50 and Marks<60):
    print("Name : ",Name)
    print("Roll No : ",RollNumber)
    print("Grade point : 6")
    print("Remarks : Pass")
else:
    print("Name : ",Name)
    print("Roll No : ",RollNumber)
    print("Grade point : 0")
    print("Remarks : Fail")

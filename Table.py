a=int(input("Enter the number to print table : "))
n=int(input("Enter the number upto which you want to print table : "))

for x in range(n):
    print(a,"*",x+1,"=",a*(x+1))
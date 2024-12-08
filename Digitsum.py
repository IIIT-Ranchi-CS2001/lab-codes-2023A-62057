a=int(input("Enter the number : "))

b=a
sum=0
while(b>0):
    sum+=b%10
    b//=10

print("Given number is :",a)
print("Sum of the digit is :",sum)
a=int(input("Enter the number of terms in series : "))

a1=0
a2=1

print("Printing Fibonacci seris :-")
if(a==1):
    print(a1)
elif(a==2):
    print(a1,a2)
else:
    b=3;
    print(a1,a2,end=" ")
    while b in range(a+1):
        an=a1+a2
        print(an,end=" ")
        a1=a2
        a2=an
        b+=1
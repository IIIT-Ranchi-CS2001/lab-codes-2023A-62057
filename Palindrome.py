s=input("Enter the string : ")

a=len(s)
flag=True
x=0
y=a-1

while x<y:
    if(s[x]!=s[y]):
        flag=False
        break
    x+=1
    y-=1

if(flag):
    print("String is palindrome")
else:
    print("String is not palindrome")
a=int(input("enter a number"))
temp=a
rev=0
num=0
while(a!=0):
    num=a%10
    rev=rev*10
    rev+=num
    a=a//10
if(rev==temp):
    print("palindrome")
else:
    print("not")

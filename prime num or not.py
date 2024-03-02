a=int(input("enter a number:\n"))
found=0
for i in range(2,a):
    if(a%i==0):
        found=1
        break
if(found==0):
    print("prime")
else:
    print("not prime")

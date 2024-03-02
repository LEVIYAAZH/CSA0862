a=eval(input("enter the new day bread: "))
b=eval(input("ent the old day bread: "))
n=185
m=0
k=0
if(a>0):
    m=n*a
    print("new loeves: ",m)
else:
    print("new bread is zero")
if(b>0):
    k=n*b*60/100
    print("old loeves: ",k)
else:
    print("old bread is zero")
print("total: ",m+k)

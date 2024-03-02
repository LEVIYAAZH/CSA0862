a=[[1,1,1],[1,1,1]]
b=[[2,2,2],[2,2,2]]
c=[[3,3,3],[3,3,3]]
d=[[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
                       c[i][j]=a[i][j]+b[i][k]+c[k][j]
for i in c:
    print("the matrix is",i)


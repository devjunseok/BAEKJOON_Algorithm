a= [1,1,2,2,2,8]
b=list(map(int,input().split()))
result=[]

for i in range(6):
    result.append(int(a[i]-b[i]))
print(*result)

import time
start=time.time()
from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    arr=input().split()
    for i in range(n):
        arr[i]=int(arr[i])
    chek=[]
    for i in range(0,n):
        if (i+1) not in arr:
            mini=i+1
        if (arr[i] in arr[0:i]) or (arr[i] in arr[i+1:n]) :
            dou=arr[i]
    #dou=d[0][0]
    print(dou,mini,sep=' ')
end=time.time()
print(end-start)
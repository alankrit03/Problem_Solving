t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    j=0
    max_sub=[]
    while(j+k<=n):
        max_sub.append(max(arr[j:j+k]))
        j+=1
    for x in max_sub:
        print(x,end=' ')
    print()
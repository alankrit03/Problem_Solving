# Enter your code here. Read input from STDIN. Print output to STDOUT

t=int(input())
for i in range(t):
    n=int(input())
    arr=input().split()
    for i in range(n):
        arr[i]=int(arr[i])
    current=  arr[0] if arr[0]>arr[-1] else arr[-1]
    arr.remove(current)
    for i in range(n-1):
        if current<arr[0] or current<arr[-1]:
            print('No')
            break
        current=  arr[0] if arr[0]>arr[-1] else arr[-1]
        arr.remove(current)
    else:
        print('Yes')
    #print(current,arr)


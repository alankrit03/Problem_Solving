def kick(arr,i):
    temp = arr.pop(i)
    arr.append(temp)
    return arr


def check(arr, k):
    lst=[]
    k_status=False
    for i in range(k,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                lst.append(arr[i])
                if i==k:
                    k_status=True
    return arr.index(min(lst)),k_status

arr = input().split()
n = len(arr)

for i in range(n):
    arr[i] = int(arr[i])

count, k = 0, 0
chk = sorted(arr)
while (chk != arr):
    z ,k_status= check(arr, k)
    arr=kick(arr,z)
    count += 1
    if z==k or not k_status:
        k+=1

print(count)
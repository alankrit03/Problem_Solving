import sys

def isprime(x):
    if x==2 or x==3:
        return True
    if x%2==0 or x%3==0:
        return False
    for i in range(5,int(x**0.5)+1,2):
        if x%i==0:
            return False
    else:return True

n = int(input())
arr = [int(x) for x in input().split()]

print(arr)

ans = 0
i = -1
j = -1

flag = 1

while j<n-1:
    if not isprime(arr[j+1]):
        j += 1
    else:
        if flag:
            j+=1
            flag = 0

        else:
            i = prev
            j+=1
        prev = j

    if flag:
        ans = max(ans, j - i)
    else:
        ans = max(ans, j - i-1)

print(ans)
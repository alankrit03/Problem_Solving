from sys import stdin, stdout

def getAns(x):
    lo, hi = 0, n-1
    while lo<hi:
        mid = (lo+hi)//2

        if final_arr[mid][1]>=x:
            hi = mid
        else:
            lo = mid+1
    return final_arr[lo][0]


n = int(stdin.readline())
arr = [int(x) for x in stdin.readline().split()]

sorted_arr = list(enumerate(arr))
sorted_arr.sort(key=lambda x:x[1])

CL = [0] * n
CR = [0] * n
temp = []

for i in range(0, n):
    while (temp and arr[temp[-1]] >= arr[i]):
        CL[i] += CL[temp[-1]] + 1
        temp.pop()
    temp.append(i)

temp = []

for i in range(n - 1, -1, -1):
    while (temp and arr[temp[-1]] > arr[i]):
        CR[i] += CR[temp[-1]] + 1
        temp.pop()
    temp.append(i)

final_arr = []
total = 0
for x in sorted_arr:
    pos = x[0]
    total += (CL[pos]+1)*(CR[pos]+1)
    final_arr.append((x[1],total))

print(final_arr)
q= int(stdin.readline())

ans = ''
for i in range(q):
    print(getAns(int(input())))

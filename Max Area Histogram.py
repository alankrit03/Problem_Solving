"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
INPUT : 6 2 5 4 5 1 6
OUTPUT: 12
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
from collections import deque

arr = [int(x) for x in input().split()]
n=len(arr)

def previous_smaller_index(arr,n):
    res = [0]*n
    stack = deque()
    stack.append(n - 1)

    for i in range(n - 2, -1, -1):

        if arr[stack[-1]] <= arr[i]:
            stack.append(i)
        else:
            while stack and arr[stack[-1]] > arr[i]:
                res[stack.pop()] = i
            stack.append(i)

    while stack:
        res[stack.pop()] = -1
    return res


def next_smaller_index(arr,n):
    res = [0]*n
    stack = deque()
    stack.append(0)

    for i in range(1, n):

        if arr[stack[-1]] <= arr[i]:
            stack.append(i)
        else:
            while stack and arr[stack[-1]] > arr[i]:
                res[stack.pop()] = i
            stack.append(i)

    while stack:
        res[stack.pop()] = n
    return res


psi = previous_smaller_index(arr,n)
nsi = next_smaller_index(arr,n)
max_area = 0
for i in range(n):
    # print(f"i={i} nsi = {nsi[i]} psi={psi[i]}")
    max_area = max(max_area , arr[i] * (nsi[i]-psi[i]-1))

print(max_area)

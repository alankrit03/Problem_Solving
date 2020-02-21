"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
INPUT : 10 7 4 3 2 9 10 11 3 2
OUTPUT: None, None, None, None, None, 2, 9, 10, 2, 2
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

from collections import deque

arr = [int(x) for x in input().split()]
n = len(arr)
result = [0] * n

stack = deque()
stack.append(n-1)

for i in range(n-2, -1,-1):

    if arr[stack[-1]] < arr[i]:
        stack.append(i)
    else:
        while stack and arr[stack[-1]] >= arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)

while stack:
    result[stack.pop()] = None

print('result = ',result)

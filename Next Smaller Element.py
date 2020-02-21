"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
INPUT : 10 7 4 3 2 9 10 11 3 2
OUTPUT : 7, 4, 3, 2, 2, 3, 3, 3, 2, None
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


from collections import deque

arr = [int(x) for x in input().split()]
n = len(arr)
result = [0] * n

stack = deque()
stack.append(0)

for i in range(1, n):

    if arr[stack[-1]] < arr[i]:
        stack.append(i)
    else:
        while stack and arr[stack[-1]] >= arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)

while stack:
    result[stack.pop()] = None

print('result = ',result)

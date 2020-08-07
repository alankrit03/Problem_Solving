"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
INPUT : 10 7 4 3 2 9 10 11 3 2
OUTPUT : 7, 4, 3, 2, 2, 3, 3, 3, 2, None
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


from collections import deque

# arr = [int(x) for x in input().split()]
arr = [10 ,7 ,4 ,3 ,2 ,9 ,10, 11, 3 ,2]
n = len(arr)
result = [0] * n

stack = deque()

for i in range(n):
    while stack and arr[stack[-1]] > arr[i]:
        result[stack[-1]] = arr[i]
        stack.pop()

    stack.append(i)

while stack:
    result[stack.pop()] = None

print('result = ',result)

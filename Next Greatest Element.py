"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
INPUT : 10   7   4   3   2   9  10 11  3   2
OUTPUT: 11, 11, 11, 11, 11, 11, 11, 3, 2, None
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
from collections import deque

arr = [int(x) for x in input().split()]
n = len(arr)
result = [0] * (n-1)
result.append(-1)
max_ = arr[-1]

for i in range(len(arr)-2, -1, -1):
    result[i] = max_
    max_ = max(max_, arr[i])

print(*result)
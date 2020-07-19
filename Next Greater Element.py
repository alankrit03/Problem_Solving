"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
INPUT : 10 7 4 3 2 9 10 11 3 2
OUTPUT: 11, 9, 9, 9, 9, 10, 11, None, None, None
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
from collections import deque

arr = [int(x) for x in input().split()]
n = len(arr)
result = [0] * n

stack = deque()
stack.append(0)

for i in range(1, n):
    """If the current element of the array is smaller than the top element of the stack
    then push the index of current element into the stack."""

    if arr[stack[-1]] >= arr[i]:
        stack.append(i)

    else:
        """Now we find an element which is larger than the top element of stack. 
        So we put that element in the result array until the element is greater than the elements in stack.
        then push current element into the stack"""
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)

while stack:
    result[stack.pop()] = None

print('result = ', result)

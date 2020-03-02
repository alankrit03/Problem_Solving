def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i;
    return -1;


# Driver Code
arr = input().split();
n = len(arr);

for i in range(len(arr)):
    arr[i]= int(arr[i])


x=int(input())
result = search(arr, n, x)
if (result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result);
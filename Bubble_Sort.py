def bubbleSort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i] , arr[j] = arr[j] , arr[i]


if __name__ == '__main__':
    # arr=input().split()
    arr = [12, 45, 23, 89, 33, 67, 25, 99, 40]
    # n = len(arr)
    # for i in range(n):
    #     arr[i] = int(arr[i])

    print(f"initial array:{arr}")
    bubbleSort(arr)
    print(f"sorted array:{arr}")

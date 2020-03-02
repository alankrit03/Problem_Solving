def selectionSort(arr):
    for i in range(len(arr)):
        temp=i
        for j in range(i+1,len(arr)):
            if arr[temp]>arr[j]:
                temp=j
        arr[temp],arr[i]=arr[i],arr[temp]

if __name__ == '__main__':
    # arr=input().split()
    arr = [12, 45, 23, 89, 33, 67, 25, 99, 40]
    # n = len(arr)
    # for i in range(n):
    #     arr[i] = int(arr[i])

    print(f"initial array:{arr}")
    selectionSort(arr)
    print(f"sorted array:{arr}")
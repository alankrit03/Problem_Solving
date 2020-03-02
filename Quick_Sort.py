def partition(arr, left, right):
    pivot = right

    while left < right:

        while (left < right and arr[left] < arr[pivot]):
            left += 1

        while (left < right and arr[right] >= arr[pivot]):
            right -= 1


        arr[left], arr[right] = arr[right], arr[left]

    if right != pivot:
        arr[pivot], arr[right] = arr[right], arr[pivot]
        return right
    return pivot



def quickSort(arr, low, high):

    if low < high:
        pivot = partition(arr, low, high)

        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)


if __name__ == '__main__':
    arr=input().split()
    #arr = [12, 45, 23, 89, 33, 67, 25, 99, 40]
    n = len(arr)
    for i in range(n):
        arr[i] = int(arr[i])

    print(f"initial array:{arr}")
    quickSort(arr, 0, n - 1)
    print(f"sorted array:{arr}")
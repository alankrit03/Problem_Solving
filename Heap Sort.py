def max_heapify(arr,n,i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l<n and arr[l]>arr[largest]:
        largest = l

    if r<n and arr[r]>arr[largest]:
        largest = r

    if largest!=i:
        arr[i],arr[largest] = arr[largest], arr[i]
        max_heapify(arr,n,largest)


def build_max_heap(arr,n):
    idx = n//2 - 1

    for i in range(idx,-1,-1):
        # print(arr)
        max_heapify(arr,n,i)

    return arr


def heap_sort(arr,n):
    arr = build_max_heap(arr,n)
    for i in range(n-1,0,-1):
        print(arr)
        arr[i],arr[0] = arr[0],arr[i]
        max_heapify(arr,i,0)
    return arr

nums = [1,2,21,33,22,98,45,23,4,5,9,3,6]

print(heap_sort(nums,len(nums)))
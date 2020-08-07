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
        print(arr)
        max_heapify(arr,n,i)

    return arr

nums = [10,8,5,6,7,2,3,11,34,54,67]
# build_heap(nums,7)

print(build_max_heap(nums,len(nums)))
def min_heapify(arr,n,i):
    smallest = i
    l = 2*i +1
    r = 2*i +2

    if l<n and arr[l]<arr[smallest]:
        smallest=l
    if r<n and arr[r]<arr[smallest]:
        smallest = r

    if smallest!=i:
        arr[i], arr[smallest] = arr[smallest],arr[i]
        min_heapify(arr,n,smallest)


def build_min_heap(arr,n):
    idx = n//2 - 1

    for i in range(idx,-1,-1):
        # print(arr)
        min_heapify(arr,n,i)

    return arr

nums = [10,8,5,6,7,2,3]
# build_heap(nums,7)

print(build_min_heap(nums,len(nums)))
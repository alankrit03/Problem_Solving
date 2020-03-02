def merge(L,R):
    len_L = len(L)
    len_R = len(R)
    arr=[]
    for _ in range(len_L+len_R):
        if L and R:
            if L[0]>=R[0]:
                arr.append(R.pop(0))
            else:
                arr.append(L.pop(0))
        else:
            if L:
                arr.extend(L)
            else:
                arr.extend(R)
            break

    return arr

def merge_sort(arr):
    n = len(arr)
    if n>1:
        L = merge_sort( arr[:n//2] )
        R = merge_sort( arr[n//2:] )
        arr=merge(L,R)
    return arr




if __name__ == '__main__':
    arr=input().split()
    # arr = [12, 45, 23, 89, 33, 67, 25, 99, 40,7]
    n = len(arr)
    for i in range(n):
        arr[i] = int(arr[i])

    print(f"initial array:{arr}")
    new_arr = merge_sort(arr)
    print(f"sorted array:{new_arr}")

    # l=[23,45,54,77,78]
    # r=[10,17,29,55,88,89,93,95]
    # this was used as test data for the merge function
    # print(*merge_sort(arr))
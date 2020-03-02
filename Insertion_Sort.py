def insert(arr,i):
    temp=arr[i]
    while i>0 and arr[i-1]>=temp:
        arr[i]=arr[i-1]
        i-=1
    arr[i]=temp



def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        insert(arr,i)
    # print(id(arr),id(x),sep='\n')

if __name__ == '__main__':
    # arr=input().split()
    arr = [12, 45, 23, 89, 33, 67, 25, 99, 40]
    # n = len(arr)
    # for i in range(n):
    #     arr[i] = int(arr[i])

    print(f"initial array:{arr}")
    # x=10
    # print(f"main function id {id(arr)} and for x is {id(20)}")
    insertionSort(arr)
    print(f"sorted array:{arr}")
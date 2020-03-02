def next_stop(arr,current):
    curr_height=arr[current]
    next_max=arr[current+1]
    pos=current+1
    for i in range(current+1,len(arr)):
        if arr[i]>=curr_height:
            return i,min(curr_height,arr[i])
        elif arr[i]>=next_max:
            next_max=arr[i]
            pos=i
    return pos,next_max

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        a=0
        water=0
        while(a<n-1):
            stop,height=next_stop(arr,a)
            print(stop,height)
            for b in range(a+1,stop):
                water+=(height-arr[b])
                a+=1
            a+=1
    print(water)
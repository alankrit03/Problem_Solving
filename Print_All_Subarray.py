arr = [98,74,12,45,6,80,70]
ans = 0
for i in range(1,len(arr)+1):
    j = 0

    while j+i<=len(arr):
        xor = 0
        for z in range(j,j+i):
            xor = xor^arr[z]

        ans ^= xor

        print(arr[j:j + i],'xor=',xor)
        j += 1

print('final ans = ',ans)
trial = 0
for i in range(len(arr)):
    trial ^= arr[i]

print(trial)
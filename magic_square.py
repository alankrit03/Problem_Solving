#MAGIC_SQUARE CRUSHED
n=int(input())
if (n%2==0):
    print('magic square not possible')
else:
    num=1
    p,q=n//2,n-1

    grid=[[0]*n for i in range(n)]
    while(num<=n**2):

        grid[p][q] = num
        p1=(p-1)%n
        q1=(q+1)%n
        #print(p1,q1)
        if(grid[p1][q1]==0):
            p=p1
            q=q1
        else:
            q=(q-1)%n
        num+=1
    for x in grid:
        for y in x: print(y,end=' ')
        print()
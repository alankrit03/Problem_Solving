# Write your code here
def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)


x, n = map(int,input().split())

x = x%10

if n>=5:
    print(1)
else:
    n = fact(n)%10
    print((x**n)%10)
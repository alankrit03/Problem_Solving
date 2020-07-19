# cook your dish here
def add_value(initial,target):
    cache = set()
    for i in range(3):
        if target[i]-initial[i]:
            cache.add(target[i]-initial[i])
            
    return len(cache)
    
    
def multiply(initial, target):
    quot = set()
    remainder = set()
    steps = 0
    for i in range(3):
        if initial[i]:
            if target[i]//initial[i]:
                quot.add(target[i]//initial[i])
            if target[i]%initial[i]:
                remainder.add(target[i]%initial[i])
        else:
            if target[i] not in remainder:
                remainder.add(target[i])
                
                
    return len(quot)+len(remainder)
    

for _ in range(int(input())):
    initial = list(map(int,input().split()))
    target = list(map(int,input().split()))
    ans = min(add_value(initial,target) , multiply(initial,target))
    print(ans)
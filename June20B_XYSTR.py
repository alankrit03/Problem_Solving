# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    pairs = idx = 0
    
    while idx<n-1:
        if s[idx]!=s[idx+1]:
            pairs += 1
            idx += 1
        idx += 1
        
    print(pairs)
        
def bin_to_int(st):
    n = len(st)
    ans = 0
    for i in range(n-1, -1, -1):
        if st[i]=='1':
            ans += 2**(n-1-i)

    return ans

print(bin_to_int('1010'))
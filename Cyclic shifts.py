'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''


# Write your code here
def int_to_bin(x):
    st = ''
    while x:
        st = str(x % 2) + st
        x //= 2

    return st


def bin_to_int(st):
    n = len(st)
    ans = 0
    for i in range(n - 1, -1, -1):
        if st[i] == '1':
            ans += 2 ** (n - 1 - i)

    return ans


for _ in range(int(input())):
    n, m, c = input().split()
    n = int(n)
    m = int(m)

    st = int_to_bin(n)
    st = '0' * (16 - len(st)) + st
    m = m % 16
    if c == 'L':
        st = st[m:] + st[:m]
    else:
        st = st[-m:] + st[:-m]

    print(bin_to_int(st))

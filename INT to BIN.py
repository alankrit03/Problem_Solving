def int_to_bin(x):
    st = ''
    while x:
        st = str(x%2) +st
        x//=2

    return st

print(int_to_bin(192))
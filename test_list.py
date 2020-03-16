def last(n):
    return n[2]


# function to sort the tuple
def sort(tuples):
    # We pass used defined function last
    # as a parameter. 
    return sorted(tuples, key=last,reverse=True)


# driver code
a = [(11, 5, 3), (7, 8, 9), (14, 12, 3)]
m = 2
print("Sorted:"),
print(sort(a))

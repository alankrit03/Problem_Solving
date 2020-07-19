# for _ in range(int(input())):
#     n, k = map(int, input().split())


def trial(n, k):
    k = ((k * 2) + 2) % n

    start = 3
    exp = 2
    while start + exp < n:
        start += exp
        exp *= 2

    final_difference = 2*(n-start+1) - 1

    k = (k+final_difference)%n

    if start + exp == n:
        return (k + 1)
    else:
        return k


# for i in range(3, 190):
#     # print(f"i={i}")
#     # a = trial(i, 26)
#     pass
#     # print(f'i={i} result = {a}')
#
# # print(trial(4,2))
# # print(trial(4,1))
# # print(trial(4,3))
# # print(trial(3,1))
# # print(trial(8,3))
print(trial(17,17))
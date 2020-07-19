def subset_sum(i, sum_):
    global even_sum

    if i == n:
        if sum_ and sum_ % 2 == 0:
            even_sum.add(sum_)
        return 0

    subset_sum(i + 1, sum_)
    subset_sum(i + 1, sum_ + arr[i])


n = int(input())

arr = [int(x) for x in input().split()]

even_sum = set()

subset_sum(0, 0)

print(len(even_sum))
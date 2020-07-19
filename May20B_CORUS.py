from collections import Counter
for _ in range(int(input())):
    n, q = map(int,input().split())

    data = input()
    cache_letter = Counter()
    cache_num = Counter()

    for x in data:
        cache_letter[x] += 1
        cache_num[cache_letter[x]] += 1

    max_rooms = max(cache_num.keys())

    for i in range(2, max_rooms + 1):
        cache_num[i] += cache_num[i-1]

    # print(cache_num)
    # print(cache_letter)
    """Input query and print answer"""
    for i in range(q):
        query = int(input())
        if query >= max_rooms:
            print(0)
        else:
            print(n-cache_num[query])
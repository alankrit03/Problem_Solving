for _ in range(int(input())):
    n = int(input())

    arr = input().split()

    for i in range(n):
        arr[i] = int(arr[i])

    best = n
    worst = curr = 1

    for i in range(1, n):
        if arr[i]-arr[i-1] <= 2:
            curr += 1

        else:
            worst = max(curr, worst)
            best = min(curr, best)
            curr = 1
    else:
        worst = max(curr, worst)
        best = min(curr, best)

    print(best, worst)
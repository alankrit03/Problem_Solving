def max_minutes(x, y, minutes):
    if x < 1 or y < 1:
        return minutes
    print(f"x={x} , y={y}")

    a = max_minutes(x + 1, y - 2, minutes + 1)
    b = max_minutes(x - 2, y + 1, minutes + 1)

    return max(a, b)


x, y = map(int, input().split())

ans = max_minutes(x, y, 0)
print(ans)
''' Read input from STDIN. Print your output to STDOUT '''


# Use input() to read input from STDIN and use print to write your output to STDOUT

def power_girl(x, r, g):
    for i in range(len(r)):
        if r[i] * x > g[i]:
            return False
    return True


def main():
    n = int(input())
    req = input().split()
    given = input().split()
    for i in range(n):
        req[i] = int(req[i])
        given[i] = int(given[i])

    l, h = 0, 2 ** 10

    while h - l > 1:
        m = (h + l) // 2

        if power_girl(m, req, given):
            l = m
        else:
            h = m

    print(l)


main()
def maze(i, j):
    global path

    if i == row - 1 and j == column - 1:
        print(*path,f'({i}, {j})')
        return 0

    if i==row or j== column or matrix[i][j] == 1:
        return 0
    else:
        path.append((i, j))
        maze(i, j + 1)
        maze(i + 1, j)
        path.pop(-1)


row, column = map(int, input().split())

matrix = []
path = []
for k in range(row):
    matrix.append([int(x) for x in input().split()])

for k in range(row):
    print(*matrix[k])

maze(0, 0)

from math import ceil
x=input().split()
# n_books, n_libraries, n_days = int(x[0]) , int(x[1]) ,int(x[2])
n_days = int(x[-1])
n_libraries = int(x[-2])
scores = [int(x) for x in input().split()]

data = []

for i in range(n_libraries):
    temp = [int(x) for x in input().split()]
    temp.append(ceil(temp[0] / temp[2]) - temp[1])
    temp2 = [int(x) for x in input().split()]
    data.append([temp, temp2])

data.sort(key=lambda x: x[0][1] )

out_n_libra = 0
total_day = 0
data_len = len(data)

while total_day < n_days and out_n_libra<data_len:
    total_day += data[out_n_libra][0][1]
    out_n_libra += 1
print(out_n_libra)
for i in range(out_n_libra):
    print(i, len(data[i][1]))
    print(*data[i][1])
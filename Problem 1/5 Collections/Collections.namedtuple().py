from collections import namedtuple

n = int(input())
columns = input().split()
Recordset = namedtuple("Recordset", columns)

data = []

for _ in range(0, n):
    v1, v2, v3, v4 = input().split()
    data.append(Recordset(v1, v2, v3, v4))

sum = 0

for recordset in data:
    sum += int(recordset.MARKS)

print("{:.2f}".format(sum / len(data)))

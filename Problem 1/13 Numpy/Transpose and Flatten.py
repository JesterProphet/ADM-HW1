import numpy


n, m = map(int, input().split())

array = []

for _ in range(0, n):
    array.append(list(map(int, input().split())))

print(numpy.transpose(array))
print(numpy.array(array).flatten())

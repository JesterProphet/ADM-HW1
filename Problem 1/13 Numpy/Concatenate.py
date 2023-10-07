import numpy


n, m, p = map(int, input().split())

array_n = []
array_m = []

for _ in range(0, n):
    array_n.append(list(map(int, input().split())))

for _ in range(0, m):
    array_m.append(list(map(int, input().split())))

array_n = numpy.array(array_n)
array_m = numpy.array(array_m)

print(numpy.concatenate((array_n, array_m), axis=0))

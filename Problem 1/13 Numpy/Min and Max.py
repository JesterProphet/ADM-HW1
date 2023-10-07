import numpy


n, m = map(int, input().split())

array = []

for _ in range(0, n):
    array.append(list(map(int, input().split())))

numpy_array = numpy.array(array)

print(numpy.min(numpy_array, axis=1).max())

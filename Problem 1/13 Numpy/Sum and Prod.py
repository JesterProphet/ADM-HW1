import numpy


n, m = map(int, input().split())

array = []

for _ in range(0, n):
    array.append(list(map(int, input().split())))

numpy_array = numpy.array(array)

print(numpy.prod(numpy.sum(numpy_array, axis=0), axis=0))

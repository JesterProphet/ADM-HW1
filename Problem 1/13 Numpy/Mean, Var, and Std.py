import numpy


n, m = map(int, input().split())

array = []

for _ in range(0, n):
    array.append(list(map(int, input().split())))

numpy_array = numpy.array(array)

print(numpy.mean(numpy_array, axis=1))
print(numpy.var(numpy_array, axis=0))
print(numpy.std(numpy_array, axis=None).round(11))

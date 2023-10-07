import numpy


n = int(input())

array_a = numpy.array([input().split() for _ in range(0, n)], int)
array_b = numpy.array([input().split() for _ in range(0, n)], int)

print(numpy.dot(array_a, array_b))

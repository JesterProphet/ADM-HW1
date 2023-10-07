import numpy


n = int(input())

array = numpy.array([input().split() for _ in range(0, n)], float)

print(numpy.linalg.det(array).round(2))

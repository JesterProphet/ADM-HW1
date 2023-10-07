import numpy


shape = tuple(map(int, input().split()))

print(numpy.zeros(shape).astype('int'))
print(numpy.ones(shape).astype('int'))

import numpy


array_a = numpy.array(input().split(), int)
array_b = numpy.array(input().split(), int)

print(numpy.inner(array_a, array_b))
print(numpy.outer(array_a, array_b))

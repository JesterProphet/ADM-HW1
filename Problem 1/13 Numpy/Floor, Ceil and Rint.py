import numpy

numpy.set_printoptions(sign=" ")


array_a = numpy.array(input().split(), float)

print(numpy.floor(array_a))
print(numpy.ceil(array_a))
print(numpy.rint(array_a))

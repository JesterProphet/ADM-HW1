import numpy


def arrays(arr):

    flipped_array = numpy.flip(list(map(float, arr)))

    return flipped_array


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
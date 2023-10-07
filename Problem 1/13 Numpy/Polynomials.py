import numpy


p = map(float, input().split())
x = float(input())

array = [number for number in p]

print(numpy.polyval(array, x))

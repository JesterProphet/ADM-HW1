import numpy


n, m = map(int, input().split())

array_a, array_b = (numpy.array([input().split() for _ in range(0, n)], int) for _ in range(0, 2))

print(array_a + array_b)
print(array_a - array_b)
print(array_a * array_b)
print(array_a // array_b)
print(array_a % array_b)
print(array_a ** array_b)

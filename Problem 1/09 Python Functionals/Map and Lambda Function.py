cube = lambda x: x**3


def fibonacci(n):

    first_number, second_number = 0, 1
    next_number = second_number

    fibonacci_series = []
    counter = 1

    if n == 1:
        fibonacci_series.append(first_number)
    elif n > 1:
        fibonacci_series.append(first_number)
        fibonacci_series.append(second_number)

    if n > 2:

        while counter < n-1:

            next_number = first_number + second_number
            first_number, second_number = second_number, next_number

            fibonacci_series.append(next_number)

            counter += 1

    return fibonacci_series


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
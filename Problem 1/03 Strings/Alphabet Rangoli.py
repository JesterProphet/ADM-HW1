def print_rangoli(size):

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    rangoli = []

    for i in range(size):
        string = "-".join(alphabet[i:size])
        rangoli.append((string[::-1] + string[1:]).center(4*size-3, "-"))

    print('\n'.join(rangoli[:0:-1] + rangoli))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
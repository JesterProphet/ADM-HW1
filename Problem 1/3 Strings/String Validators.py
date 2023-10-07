if __name__ == '__main__':

    s = input()
    l = list(s)

    for i in range(0, len(l)):
        if l[i].isalnum():
            check = "True"
            break
        else:
            check = "False"

    print(check)

    for i in range(0, len(l)):
        if l[i].isalpha():
            check = "True"
            break
        else:
            check = "False"

    print(check)

    for i in range(0, len(l)):
        if l[i].isdigit():
            check = "True"
            break
        else:
            check = "False"

    print(check)

    for i in range(0, len(l)):
        if l[i].islower():
            check = "True"
            break
        else:
            check = "False"

    print(check)

    for i in range(0, len(l)):
        if l[i].isupper():
            check = "True"
            break
        else:
            check = "False"

    print(check)

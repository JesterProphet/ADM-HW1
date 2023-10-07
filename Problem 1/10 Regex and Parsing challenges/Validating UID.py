t = int(input())

for _ in range(0, t):

    uid = str(input())
    output = "Invalid"

    if len([char for char in uid if (char.isalpha() and char.isupper())]) >= 2:
        if len([char for char in uid if char.isnumeric()]) >= 3:
            if len([char for char in uid if (char.isalpha() or char.isnumeric())]) == 10:
                if len([char for char in uid if uid.count(char) == 1]) == 10:
                    if len(uid) == 10:
                        output = "Valid"

    print(output)

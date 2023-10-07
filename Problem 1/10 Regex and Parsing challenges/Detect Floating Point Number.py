import re


t = int(input())

for _ in range(0, t):

    input_string = input()
    output = False

    if input_string.count(".") == 1 and input_string[-1] != ".":
        if not re.match(r'[A-Za-z]', input_string):
            if input_string[0] in "+-":
                if input_string[1] in "0123456789.":
                    output = True
            elif input_string[0] == ".":
                if input_string[1] in "0123456789":
                    output = True
            else:
                if input_string.count("+") == 0 and input_string.count("-") == 0:
                    output = True

    try:
        float(input_string)
    except:
        output = False

    print(output)

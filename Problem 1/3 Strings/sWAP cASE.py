def swap_case(s):

    input_string = list(s)

    for i in range(0, len(s)):
        if s[i].islower():
            input_string[i] = chr(ord(s[i]) - 32)
        elif s[i].isupper():
            input_string[i] = chr(ord(s[i]) + 32)
        else:
            pass

    output_string = ''.join(input_string)

    return output_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
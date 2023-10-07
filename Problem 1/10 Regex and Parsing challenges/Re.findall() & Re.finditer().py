def is_vowel(char):
    if char in "AEIOUaeiou":
        return True
    else:
        return False


input_string = input()
check_for_print = False

i = 0

while i < len(input_string):

    if is_vowel(input_string[i]):

        output = input_string[i]
        search = True
        i += 1

        while search and i < len(input_string):
            if is_vowel(input_string[i]):
                output = output + input_string[i]
                i += 1
            else:
                search = False

        if len(output) > 1 and not input_string.endswith(output):
            print(output)
            check_for_print = True

    i += 1

if not check_for_print:
    print(-1)

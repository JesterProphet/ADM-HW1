def merge_the_tools(string, k):

    split_string = []

    for i in range(0, len(string), k):
        split_string.append(string[i:i+k])

    for i in range(0, len(split_string)):
        split_string[i] = "".join(dict.fromkeys(split_string[i]))

    for sub_string in split_string:
        print(sub_string)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
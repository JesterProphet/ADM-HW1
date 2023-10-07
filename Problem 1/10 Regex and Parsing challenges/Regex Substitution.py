n = int(input())

for _ in range(0, n):

    input_string = str(input())

    while input_string.count(" && "):
        input_string = input_string.replace(" && ", " and ")

    while input_string.count(" || "):
        input_string = input_string.replace(" || ", " or ")

    print(input_string)

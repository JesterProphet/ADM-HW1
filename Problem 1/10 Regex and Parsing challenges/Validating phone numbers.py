n = int(input())

for _ in range(0, n):

    input_string = input()

    try:
        if len(input_string) == 10 and input_string[0] in "789" and int(input_string):
            print("YES")
        else:
            print("NO")
    except:
        print("NO")

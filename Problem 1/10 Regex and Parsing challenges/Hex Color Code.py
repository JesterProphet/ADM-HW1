import re


n = int(input())

for _ in range(0, n):

    code_line = input()

    output = re.findall(r':?.#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})', code_line)

    if output:
        for element in output:
            print("#" + element)

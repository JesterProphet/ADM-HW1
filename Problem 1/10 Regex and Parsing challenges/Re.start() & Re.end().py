import re


input_string = input()
search_string = input()

output = re.finditer(f'(?=({search_string}))', input_string)

check = False

for element in output:
    print((element.start(1), element.end(1)-1))
    check = True

if not check:
    print((-1, -1))

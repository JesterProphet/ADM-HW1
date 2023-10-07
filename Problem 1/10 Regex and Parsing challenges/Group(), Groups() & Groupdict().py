import re


input_string = input()

split_string = [item[0] for item in re.findall(r"((.)\2*)", input_string)]
new_string = [item for item in split_string if len(item) > 1 and (item.isalpha() or item.isnumeric())]

if new_string:
    print(new_string[0][0])
else:
    print(-1)

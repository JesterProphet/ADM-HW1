import re


n = int(input())

for _ in range(0, n):

    name, email = input().split()

    if re.match(r'^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$', email):
        print(name, email)


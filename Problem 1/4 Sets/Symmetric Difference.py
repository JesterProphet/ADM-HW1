m = input()
set1 = set(map(int, input().split(' ')))

n = input()
set2 = set(map(int, input().split(' ')))

difference = []

for item in (set1 - set2):
    difference.append(item)

for item in (set2 - set1):
    difference.append(item)

for item in sorted(difference):
    print(item)

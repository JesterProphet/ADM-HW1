n, m = map(int, input().split(' '))
array = list(map(int, input().split(' ')))
set1 = set(map(int, input().split(' ')))
set2 = set(map(int, input().split(' ')))

happiness_score = 0

for item in array:
    if item in set1:
        happiness_score += 1
    elif item in set2:
        happiness_score -= 1

print(happiness_score)


n = int(input())
roll_number_set1 = set(map(int, input().split()))

b = int(input())
roll_number_set2 = set(map(int, input().split()))

union_set = set(roll_number_set1) | set(roll_number_set2)

print(len(union_set))

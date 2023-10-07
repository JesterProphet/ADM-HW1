n = int(input())
roll_number_set1 = set(map(int, input().split()))

b = int(input())
roll_number_set2 = set(map(int, input().split()))

symmetric_difference_set = roll_number_set1 ^ roll_number_set2

print(len(symmetric_difference_set))

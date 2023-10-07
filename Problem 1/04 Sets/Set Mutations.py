a = int(input())
set1 = set(map(int, input().split()))
N = int(input())

for _ in range(0, N):

    command = input().split()
    set2 = set(map(int, input().split()))

    if command[0] == "update":
        set1.update(set2)
    elif command[0] == "intersection_update":
        set1.intersection_update(set2)
    elif command[0] == "difference_update":
        set1.difference_update(set2)
    elif command[0] == "symmetric_difference_update":
        set1.symmetric_difference_update(set2)

print(sum(set1))

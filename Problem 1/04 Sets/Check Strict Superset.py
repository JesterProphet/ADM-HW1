set_a = set(map(int, input().split()))
n = int(input())

is_superset = True
count = 0

while is_superset and count < n:

    set_b = set(map(int, input().split()))

    if set_a.issuperset(set_b):
        is_superset = True
    else:
        is_superset = False

    count += 1

print(is_superset)

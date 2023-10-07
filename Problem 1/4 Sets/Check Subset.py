t = int(input())

for _ in range(0, t):

    lenght_a = int(input())
    set_a = set(map(int, input().split()))

    lenght_b = int(input())
    set_b = set(map(int, input().split()))

    print(set_a.issubset(set_b))

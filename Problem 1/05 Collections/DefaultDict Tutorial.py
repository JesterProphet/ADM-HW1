variables = list(map(int, input().split()))

n = variables[0]
m = variables[1]

a = list()
b = list()

for _ in range(0, n):
    a.append(input())

for _ in range(0, m):
    b.append(input())

for word_b in b:

    output_list = " ".join([str(i+1) for i, word_a in enumerate(a) if word_a == word_b])

    if output_list:
        print(output_list)
    else:
        print(-1)

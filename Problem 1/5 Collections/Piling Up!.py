from collections import deque

t = int(input())

for _ in range(0, t):

    n = int(input())
    d = deque(map(int, input().split()))

    last_element = 10000000000000000000
    stackable = "Yes"

    while stackable == "Yes" and d:

        if len(d) == 1 and d[0] <= last_element:
            d.pop()
        elif len(d) > 1 and d[-1] <= d[0] <= last_element:
            last_element = d[0]
            d.popleft()
        elif len(d) > 1 and d[0] < d[-1] <= last_element:
            last_element = d[-1]
            d.pop()
        else:
            stackable = "No"

    print(stackable)

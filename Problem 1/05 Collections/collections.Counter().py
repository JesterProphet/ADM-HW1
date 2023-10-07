x = int(input())
shoe_size_list = input().split()

n = int(input())
earnings = 0

for _ in range(0, n):

    shoe_size, price = input().split()

    if shoe_size in shoe_size_list:
        earnings += int(price)
        shoe_size_list.remove(shoe_size)

print(earnings)

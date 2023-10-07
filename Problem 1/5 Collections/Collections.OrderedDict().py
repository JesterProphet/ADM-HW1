from collections import OrderedDict

basket = []
ordered_dict = OrderedDict()

n = int(input())

for _ in range(0, n):
    product, space, price = input().rpartition(' ')
    basket.append(product)
    ordered_dict[product] = price

for item in ordered_dict:
    net_price = int(basket.count(item)) * int(ordered_dict[item])
    print(f"{item} {net_price}")

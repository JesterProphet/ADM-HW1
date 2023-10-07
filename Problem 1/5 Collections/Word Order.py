from collections import OrderedDict

l = []
ordered_dict = OrderedDict()

n = int(input())

for _ in range(0, n):

    word = str(input())
    l.append(word)

    if word in ordered_dict:
        ordered_dict[word] += 1
    else:
        ordered_dict[word] = 1

print(len(ordered_dict))
print(" ".join([str(ordered_dict[word]) for word in ordered_dict]))

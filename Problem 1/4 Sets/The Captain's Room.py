k = int(input())
room_number_list = list(map(int, input().split()))
room_number_set = set(room_number_list)

for room in room_number_set:
    room_number_list.remove(room)

print(room_number_set.difference(set(room_number_list)).pop())

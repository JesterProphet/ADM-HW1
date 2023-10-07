import calendar

month, day, year = map(int, input().split())

weekday = calendar.weekday(year, month, day)

if weekday == 0:
    weekday_label = "MONDAY"
elif weekday == 1:
    weekday_label = "TUESDAY"
elif weekday == 2:
    weekday_label = "WEDNESDAY"
elif weekday == 3:
    weekday_label = "THURSDAY"
elif weekday == 4:
    weekday_label = "FRIDAY"
elif weekday == 5:
    weekday_label = "SATURDAY"
elif weekday == 6:
    weekday_label = "SUNDAY"

print(weekday_label)

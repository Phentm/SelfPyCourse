from calendar import weekday

user_date = input("Enter a date: ")

day = int(user_date[:2])
month = int(user_date[3:5])
year = int(user_date[6:])

weekday = weekday(year, month, day)

if weekday == 0:
    print("Monday")
elif weekday == 1:
    print("Tuesday")
elif weekday == 2:
    print("Wednesday")
elif weekday == 3:
    print("Thursday")
elif weekday == 4:
    print("Friday")
elif weekday == 5:
    print("Saturday")
elif weekday == 6:
    print("Sunday")


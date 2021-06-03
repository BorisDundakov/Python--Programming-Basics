hour = int(input())
weekday = input()
is_open = False
if 10 <= hour <= 18:
    if weekday == "Monday" or weekday == "Tuesday" or weekday == "Wednesday" or weekday == "Thursday" or weekday == "Friday" or weekday == "Saturday":
       is_open = True
if is_open:
    print("open")
else:
    print("closed")





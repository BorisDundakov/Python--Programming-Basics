age = float(input())
gender = input()

if age >= 16:
    if gender == "m":
        print("Mr.")
    else:
        print("Ms.")
elif age < 16:
    if gender == "m":
        print("Master")
    elif gender == "f":
        print("Miss")




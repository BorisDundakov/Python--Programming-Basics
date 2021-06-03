project_type = input()
rows = int(input())
columns = int(input())

if project_type == "Premiere":
    price = 12
elif project_type == "Normal":
    price = 7.5
elif project_type == "Discount":
    price = 5


total_expense = price * rows * columns
print(f"{total_expense :.2f}")
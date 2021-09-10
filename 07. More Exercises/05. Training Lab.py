w = float(input())
h = float(input())

hall_width = h * 100
space_for_desk = hall_width - 100
n_desks = space_for_desk // 70

hall_height = w * 100
rows = hall_height // 120

seats = rows * n_desks - 3
print(f"{seats :.0f}")



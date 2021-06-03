width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())
available_space = width_free_space * length_free_space * height_free_space
# Всеки кашон е с точни размери:  1m x 1m x 1m.
command = input()
while command != "Done":
    boxes = int(command)
    available_space -= boxes
    if available_space <= 0:
        print(f"No more free space! You need {abs(available_space)} Cubic meters more.")

        break
    command = input()

else:
    print(f"{available_space} Cubic meters left.")



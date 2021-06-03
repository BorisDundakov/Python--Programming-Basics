type_flours = input()
num_flours = int(input())
budget = int(input())

final_price = 0
remaining_sum = 0

if type_flours == "Roses":
    if num_flours > 80:
        final_price = num_flours * (5 * 0.9)
    else:
        final_price = num_flours * 5

elif type_flours == "Dahlias":
    if num_flours > 90:
        final_price = num_flours * (3.8 * 0.85)
    else:
        final_price = num_flours * 3.8

elif type_flours == "Tulips":
    if num_flours > 80:
        final_price = num_flours * (2.8 * 0.85)
    else:
        final_price = num_flours * 2.8

elif type_flours == "Narcissus":
    if num_flours < 120:
        final_price = num_flours * (3 * 1.15)
    else:
        final_price = num_flours * 3

elif type_flours == "Gladiolus":
    if num_flours < 80:
        final_price = num_flours * (2.5 * 1.20)
    else:
        final_price = num_flours * 2.5


remaining_sum = abs(budget - final_price)

if budget >= final_price:
    print(f"Hey, you have a great garden with {num_flours} {type_flours} and {remaining_sum :.2f} leva left.")
else:
    print(f"Not enough money, you need {remaining_sum :.2f} leva more.")



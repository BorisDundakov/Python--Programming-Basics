budget = float(input())
n_extras = int(input())
clothing_price = float(input())

decor = 0.10 * budget
if n_extras > 150:
    clothing_price= clothing_price * 0.9

total_costs = n_extras * clothing_price + decor
remaining_money = budget - total_costs


if total_costs > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(remaining_money):.2f} leva more.")
elif total_costs <= budget:
    print("Action!")
    print(f"Wingard starts filming with {abs(remaining_money):.2f} leva left.")
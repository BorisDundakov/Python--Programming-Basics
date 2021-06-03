budget = int(input())
season = input()
n_fisherman = int(input())
ship_price = 0
remaining_sum = 0

if season == "Spring":
    ship_price = 3000

elif season == "Summer" or season == "Autumn":
    ship_price = 4200

elif season == "Winter":
    ship_price = 2600

if n_fisherman <= 6:
    ship_price = ship_price * 0.9

elif 7 <= n_fisherman <= 11:
    ship_price = ship_price * 0.85

elif n_fisherman > 12:
    ship_price = ship_price * 0.75

if n_fisherman % 2 == 0:
    if season != "Autumn":
        ship_price = ship_price * 0.95


remaining_sum = abs(budget - ship_price)

if budget >= ship_price:
    print(f"Yes! You have {remaining_sum :.2f} leva left.")
else:
    print(f"Not enough money! You need {remaining_sum :.2f} leva.")

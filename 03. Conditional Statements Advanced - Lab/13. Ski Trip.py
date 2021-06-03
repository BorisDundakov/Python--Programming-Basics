days = int(input())
flat = input()
mark = input()
price_flat = 0
nights_price = 0
nights = days - 1

if flat == "room for one person":
    nights_price = 18
    price_flat = nights_price * nights

elif flat == "apartment":
    nights_price = 25
    if days < 10:
        price_flat = (nights_price * nights) * 0.7
    elif 10 < days < 15:
        price_flat = (nights_price * nights) * 0.65
    else:
        price_flat = (nights_price * nights) * 0.5

elif flat == "president apartment":
    nights_price = 35
    if days < 10:
        price_flat = (nights_price * nights) * 0.9
    elif 10 < days < 15:
        price_flat = (nights_price * nights) * 0.85
    else:
        price_flat = (nights_price * nights) * 0.8

if mark == "positive":
    final_price = price_flat + 0.25 * price_flat
elif mark == "negative":
    final_price = price_flat - 0.10 * price_flat

print(f"{final_price :.2f}")



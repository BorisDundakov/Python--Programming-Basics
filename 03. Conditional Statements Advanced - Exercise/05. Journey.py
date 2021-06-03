budget = float(input())
season = input()
country = ""
price = 0
if budget <= 100:
    country = "Somewhere in Bulgaria"
    if season == "winter":
        price = 0.7 * budget
        building = "Hotel"

    elif season == "summer":
        price = 0.3 * budget
        building = "Camp"

elif budget <= 1000:
    country = "Somewhere in Balkans"
    if season == "winter":
        price = 0.8 * budget
        building = "Hotel"

    elif season == "summer":
        price = 0.4 * budget
        building = "Camp"

elif budget >= 1000:
    country = "Somewhere in Europe"
    price = 0.9 * budget
    building = "Hotel"

print(f"{country}")
print(f"{building} - {price :.2f}")



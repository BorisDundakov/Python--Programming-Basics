month = input()
n_nights = int(input())
studio = 0
apartment = 0
price_apartment = 0
price_studio = 0
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < n_nights < 14 :
        price_studio = studio * 0.95 * n_nights
        price_apartment = apartment * n_nights
    if n_nights > 14:
        price_studio = studio * 0.70 * n_nights
        price_apartment = apartment * 0.90 * n_nights
    else:
        price_apartment = apartment * n_nights
        price_studio = studio * n_nights

elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if n_nights > 14:
        price_studio = studio * 0.80 * n_nights
        price_apartment = apartment * 0.90 * n_nights
    else:
        price_apartment = apartment * n_nights
        price_studio = studio * n_nights

elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if n_nights > 14:
        price_apartment = apartment * 0.90 * n_nights
        price_studio = studio * n_nights
    else:
        price_apartment = apartment * n_nights
        price_studio = studio * n_nights

print(f"Apartment: {price_apartment :.2f} lv.")
print(f"Studio: {price_studio :.2f} lv.")


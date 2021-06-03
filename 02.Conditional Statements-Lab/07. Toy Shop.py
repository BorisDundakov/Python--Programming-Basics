
puzzle = 2.60
talking_doll = 3.00
teddy_bear = 4.10
minion = 8.20
truck = 2.00

trip_prize = float(input())
n_puzzles = int(input())
n_talking_doll = int(input())
n_teddy_bears = int(input())
n_minion = int(input())
n_truck = int(input())

total_toys = n_puzzles + n_talking_doll + n_teddy_bears + n_minion + n_truck
income = n_puzzles * puzzle + talking_doll * n_talking_doll + teddy_bear\
         * n_teddy_bears + minion * n_minion + truck\
         * n_truck

if total_toys >= 50:
    discount = income * 0.25
    final_price = income - discount
    rent = final_price * 0.10
    profit = final_price - rent
    if profit >= trip_prize:
        print(f"Yes! {profit - trip_prize :.2f} lv left.")
    else:
        print(f"Not enough money! {trip_prize - profit :.2f} lv needed.")

else:
    rent = income * 0.10
    profit = income - rent
    if profit >= trip_prize:
        print(f"Yes! {profit - trip_prize :.2f} lv left.")
    else:
        print(f"Not enough money! {trip_prize - profit :.2f} lv needed.")


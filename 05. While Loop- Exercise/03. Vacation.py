needed_money = float(input())
available_money = float(input())
next_sum = 0
spending_counter = 0
total_days = 0
type_activity = ''
can_save_money = True

while spending_counter < 5:
    type_activity = input()
    next_sum = float(input())

    if type_activity == 'spend':
        total_days += 1
        available_money = available_money - next_sum
        spending_counter += 1
        if available_money < 0:
            available_money = 0

    elif type_activity == 'save':
        available_money = available_money + next_sum
        total_days += 1
        spending_counter = 0

    if available_money >= needed_money:
        can_save_money = True
        break


else:

    can_save_money = False


if can_save_money:
    print(f"You saved the money for {total_days} days.")
else:
    print("You can't save the money.")
    print(total_days)

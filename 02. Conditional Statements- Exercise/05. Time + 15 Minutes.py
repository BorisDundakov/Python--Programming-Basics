# Да се напише програма, която чете час и минути от 24-часово денонощие, въведени от потребителя и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат часове:минути. Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59.
# Часовете се изписват с една или две цифри. Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.
# Примерен вход и изход
# вход	изход		вход	изход		вход	изход		вход	изход		вход	изход
# 1
# 46	2:01		0
# 01	0:16		23
# 59	0:14		11
# 08	11:23		12
# 49	13:04

hours = int(input())
minutes = int(input())
add_minutes = minutes + 15
if add_minutes >= 60:
    total_hours = hours + 1
    if total_hours > 23:
        total_hours= total_hours - 24
        total_minutes = add_minutes - 60
        if total_minutes > 9:
            print(f"{total_hours}:{total_minutes} ")
        else:
            print(f"{total_hours}:0{total_minutes} ")

    else:
        total_minutes = add_minutes - 60
        if total_minutes > 9:
            print(f"{total_hours}:{total_minutes} ")
        else:
            print(f"{total_hours}:0{total_minutes} ")
elif add_minutes < 60:
    print(f"{hours}:{add_minutes}")



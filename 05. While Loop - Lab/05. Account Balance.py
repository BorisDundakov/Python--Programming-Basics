command = (input())
total_sum = 0
while command != "NoMoreMoney":
    command = float(command)
    if command >= 0:
        print(f"Increase: {command :.2f}")
        total_sum += command
        command = input()
    else:
        print("Invalid operation!")
        print(f"Total: {total_sum}")
        break

else:
    print(f"Total: {total_sum :.2f}")


command = input()
sum_command = 0
sum_prime_numbers = 0
sum_non_prime_numbers = 0

# просто число -> четно число, с излкючение на 2
while command != "stop":
    is_Prime = True
    number = int(command)
    if number < 0:
        print("Number is negative.")
        command = input()
        continue
    else:
        for checking in range (2, number):  # range (диапазон, в които)
            if number % checking == 0:  # (си проверявам дали се дели числото)
                is_Prime = False
                break

        if is_Prime:
            sum_prime_numbers += number
        else:
            sum_non_prime_numbers += number
    command = input()
print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")
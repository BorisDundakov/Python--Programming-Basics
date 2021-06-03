first_number = int(input())
second_number = int(input())


for number in range(first_number, second_number + 1):
    number_as_string = str(number)
    sum_even = 0
    sum_odd = 0
    for index, digit in enumerate(number_as_string):
        if index % 2 == 0: # индекса винаги започва от 0, за това са обърнати
            sum_odd += int(digit)
        else:
            sum_even += int(digit)

    if sum_odd == sum_even:
        print(f"{number_as_string}", end = " ")



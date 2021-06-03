n = int(input())
if n > 0:
    for first_digit in range(1, 9):
        if n % first_digit == 0:
            for second_digit in range(1, 9):
                if n % second_digit == 0:
                    for third_digit in range(1, 9):
                        if n % third_digit == 0:
                            for forth_digit in range(1, 9):
                                if n % forth_digit == 0:
                                    print(f'{first_digit}{second_digit}{third_digit}{forth_digit}', end =" ")




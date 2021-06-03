n = int(input())
l = int(input())
# ASCI TABLE EXERCISE
for first in range (1, n+1):
    for second in range (1, n+1):
        for third in range (97, 97 + l):  # стойностите от аски таблицата
                                          # от 97 започват малките букви
            for forth in range (97, 97 + l):
                for fifth in range (1, n+1):
                    if fifth > first and fifth > second:
                        print(f'{first}{second}{chr(third)}{chr(forth)}{fifth}', end = " ")




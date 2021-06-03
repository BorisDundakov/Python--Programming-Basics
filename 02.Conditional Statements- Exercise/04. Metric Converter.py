# Да се напише програма, която преобразува разстояние между следните 3 мерни единици: mm, cm, m. Използвайте съответствията от таблицата по-долу:
# входна единица	изходна единица
# 1 meter (m)	1000 millimeters (mm)
# 1 meter (m)	100 centimeters (cm)
# Входните данни се състоят от три реда, въведени от потребителя:
# •	Първи ред: число за преобразуване - реално число;
# •	Втори ред: входна мерна единица – текст;
# •	Трети ред: изходна мерна единица (за резултата) – текст.
# На конзолата да се отпечата резултатът от преобразуването на мерните единици, форматиран до третия знак след десетичната запетая.
# вход	изход		вход	изход		вход	изход
# 12
# mm
# m	0.012		150
# m
# cm	15000.000		45
# cm
# mm	450.000


conversion_number = float(input())
measurement_unit = str(input())
convert_unit = str(input())

if measurement_unit == "mm" and convert_unit =="m":
    print(f"{conversion_number / 1000 :.3f}")
elif measurement_unit == "mm" and convert_unit =="cm":
    print(f"{conversion_number / 10 :.3f}")
elif measurement_unit == "cm" and convert_unit =="m":
    print(f"{conversion_number / 100 :.3f}")
elif measurement_unit == "cm" and convert_unit =="mm":
    print(f"{conversion_number * 10 :.3f}")
elif measurement_unit == "m" and convert_unit =="cm":
    print(f"{conversion_number * 100 :.3f}")
elif measurement_unit == "m" and convert_unit =="mm":
    print(f"{conversion_number * 1000 :.3f}")



from math import floor

income_in_lv = float(input())
average_grade = float(input())
min_wage = float(input())

if average_grade >= 5.50:
    scholarship = average_grade * 25
    print(f"You get a scholarship for excellent results {floor(scholarship)} BGN")

elif min_wage > income_in_lv and average_grade > 4.50:
    scholarship = 0.35 * min_wage
    print(f"You get a Social scholarship {floor(scholarship)} BGN")

else:
    print("You cannot get a scholarship!")

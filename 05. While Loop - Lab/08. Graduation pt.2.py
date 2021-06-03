name = input()
grade = 1
sum_score = 0
excluded = 0
while grade <= 12:
    score = float(input())
    if score < 4:
        excluded += 1
        if excluded == 2:
            break
    else:
        sum_score += score
        grade += 1
if excluded == 2:
    print(f"{name} has been excluded at {grade} grade")
else:
    print(f"{name} graduated. Average grade: {sum_score / 12:.2f}")

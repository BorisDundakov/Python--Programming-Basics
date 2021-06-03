n_jury = int(input())
name_presentation = input()
final_grade = 0
grade_number = 0
while name_presentation != "Finish":

    average_grade = 0
    for grades in range (n_jury):
        current_grade = float(input())
        average_grade += current_grade
        grade_number += 1
        final_grade += current_grade

    average_grade /= n_jury
    print(f'{name_presentation} - {average_grade :.2f}.')
    name_presentation = input()

final_assessment = 0

print(f"Student's final assessment is {final_grade /grade_number :.2f}.")


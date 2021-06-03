import sys

max_number = -sys.maxsize
n = int(input())
total_sum = 0
for i in range(0, n):
    number = int(input())

    if number > max_number:
        max_number = number

    total_sum += number

if max_number == total_sum - max_number:
    print("Yes")
    print(f"Sum = {total_sum - max_number}")

else:
    print("No")
    sum_others = abs(max_number - (total_sum - max_number))
    print(f"Diff = {abs(sum_others)}")

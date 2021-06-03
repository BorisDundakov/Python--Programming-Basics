from math import floor

record_in_seconds = float(input())
distance_in_metres = float(input())
time_in_seconds_per_meter = float(input())

# съпротивлението на водата го забавя на всеки 15 метра с 12.5 секунди.

time_in_seconds_required = distance_in_metres * time_in_seconds_per_meter
resistance = (distance_in_metres / 15)
new_resistance = floor(resistance)
new_resistance = new_resistance * 12.5
total_time = time_in_seconds_required + new_resistance
time_left = total_time - record_in_seconds
if record_in_seconds <= total_time:
    print(f"No, he failed! He was {time_left :.2f} seconds slower.")
elif record_in_seconds > total_time:
    print(f" Yes, he succeeded! The new world record is {total_time :.2f} seconds.")


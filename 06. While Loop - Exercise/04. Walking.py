number_steps = input()
steps_goal = 10000
steps_home = 0
goal_reached = False
total_steps = 0
final_total_steps = 0

while number_steps != 'Going home':
    number_steps = int(number_steps)
    total_steps += number_steps
    if total_steps < steps_goal:
        pass
    else:
        final_total_steps = total_steps
        goal_reached = True
        break

    number_steps = input()

else:
    steps_home = int(input())
    total_steps = total_steps + steps_home
    final_total_steps = total_steps


if total_steps >= steps_goal:
    goal_reached = True
else:
    goal_reached = False

steps_difference = abs(total_steps - steps_goal)

if goal_reached:
    print("Goal reached! Good job!")
    print(f"{steps_difference} steps over the goal!")
else:
    print(f"{steps_difference} more steps to reach goal.")
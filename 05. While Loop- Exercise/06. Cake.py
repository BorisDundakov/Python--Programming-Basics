cake_height = int(input())
cake_width = int(input())
command = input()
having_cake = True
taken_pieces = 0
cake_size = cake_height * cake_width
remaining_pieces = 0

while command != "STOP":
    command = int(command)
    taken_pieces += command
    remaining_pieces = (cake_size - taken_pieces)
    if remaining_pieces < 0:
        having_cake = False
        break
    command = input()  # VERY IMPORTANT LINE DON'T FORGET IT!!!

else:
    having_cake = True

if having_cake:
    print(f"{remaining_pieces} pieces are left." )

else:
    print(f"No more cake left! You need {abs(remaining_pieces)} pieces more.")

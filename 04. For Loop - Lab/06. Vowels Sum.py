text = str(input())
score = 0
for position in text:
    if position == "a":
        score += 1
    if position == "e":
        score += 2
    if position == "i":
        score += 3
    if position == "o":
        score += 4
    if position == "u":
        score += 5

print(score)










for first in range (1, 11):
    for second in range (1, 11): # обходи всички втори множители от 1 до 10.
        result = first * second # Вторият множител се сменя, първия си стои, докато не стигнем до 10
        print(f"{first}* {second} = {result}")
book = input() # yes
next_book = input() # yes
number = 0 # yes
while next_book != book: #
    next_book = input() #
    number += 1 #
    if next_book == "No More Books": #
        print("The book you search is not here!") #
        print(f"You checked {number} books.") #
else:
   print(f"You checked {number} books and found it.") #





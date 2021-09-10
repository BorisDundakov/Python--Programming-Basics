price_kg_vegetables = float(input())
price_kg_fruit = float(input())
total_kg_vegetables = float(input())
total_kg_fruit = float(input())

total_bgn = price_kg_fruit * total_kg_fruit + price_kg_vegetables * total_kg_vegetables
total_euro = total_bgn / 1.94
print(f"{total_euro :.2f}")

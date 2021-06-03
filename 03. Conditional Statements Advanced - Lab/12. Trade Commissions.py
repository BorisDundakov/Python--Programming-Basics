city_name = input()
sales =  float(input())
commission = 0
total_sales = 0

if city_name == "Sofia":
    if 0 <= sales <= 500:
        commission = 0.05
        total_sales = commission * sales
    elif 500 <= sales <= 1000:
        commission = 0.07
        total_sales = commission * sales
    elif 1000 <= sales <= 10000:
        commission = 0.08
        total_sales = commission * sales
    elif sales >= 10000:
        commission = 0.12
        total_sales = commission * sales
    else:
       total_sales == 0


elif city_name == "Varna":
    if 0 <= sales <= 500:
        commission = 0.045
        total_sales = commission * sales
    elif 500 <= sales <= 1000:
        commission = 0.075
        total_sales = commission * sales
    elif 1000 <= sales <= 10000:
        commission = 0.10
        total_sales = commission * sales
    elif sales >= 10000:
        commission = 0.13
        total_sales = commission * sales

    else:
        total_sales == 0


elif city_name == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 0.055
        total_sales = commission * sales
    elif 500 <= sales <= 1000:
        commission = 0.08
        total_sales = commission * sales
    elif 1000 <= sales <= 10000:
        commission = 0.12
        total_sales = commission * sales
    elif sales >= 10000:
        commission = 0.145
        total_sales = commission * sales

    else:
        total_sales == 0

else:
    total_sales == 0

if total_sales == 0:
    print("error")

else:
    print(f"{total_sales :.2f} ")




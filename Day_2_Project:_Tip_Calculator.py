print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
how_many_people = int(input("How many people to split the bill? "))
total_bill_with_tip = total_bill * (percentage + 100) / 100
print(f"Each people should pay ${round(total_bill_with_tip / how_many_people,2)}")
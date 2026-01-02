print("Welcome to the tip calculator!")
bill = float(input("What was the total bill in EUR? "))
tip_percent = float(input("How much tip would you like to give (in percentage)? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

percent = tip_percent / 100

tip_value = percent * bill
bill_per_person = round((bill + tip_value)/number_of_people, 2)

print(f"Each person should pay: {bill_per_person:.2f} EUR")
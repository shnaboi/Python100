# Tip Calculator

print("Welcome to the tip calculator")
bill = float(input("What was the toal bill amount? $"))
perc = .01 * float(input("What % tip would you like to give? "))
split = float(input("How many people will splut the bill? "))
taxed_bill = (bill * perc) + bill
print(taxed_bill)
ans_float = (taxed_bill / split)
ans_round = round(ans_float, 2)
print(f"Total amount = ${round(taxed_bill, 2)}")
print(f"Everyone pays ${ans_round}")


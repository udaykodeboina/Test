from decimal import Decimal 
a = int(input("How many working days: "))

"""
This is a mothly payable calculation
"""
b = int(input("Enter the daily allowance per day: ")) # daily allowance
c = a * b
d = Decimal(c * 0.27)
e = c - d
print ("No of days in a month are:", a)
print ("Daily allowance per day is:", b)
print("Monthly Expected: ", c)
print("tax Payable", round(d,2))
print("Remaining monthly is:", round(e,2))


from decimal import Decimal 
a = 22 #total number of days

"""
This is a mothly payable calculation
"""
b = 600 # daily allowance
c = a * b
d =Decimal(c * 0.27)
e = c - d
print ("No of days in a month are:", a)
print ("Daily allowance per day is:", b)
print("Monthly Expected: ", c)
print("tax Payable", round(d,2))
print("Remaining monthly is:", e)

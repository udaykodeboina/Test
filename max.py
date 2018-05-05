a=int(input("enter first value:"))
b=int(input("enter second value:"))
c=int(input("enter third value:"))
max=a if a>b and a>c else b if b>c else c
print("maximum value is:",max)
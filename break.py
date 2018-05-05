cart=[10,20,30,40,600,70,90]
for item in cart:
    if item>500:
        print("sorry cant process")
        break
    print("processing item:",item)
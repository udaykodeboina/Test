#compute bill for a super market
groceries = ["apple","banana", "orange","pear"]#'enter groceries'

stock = {"banana": 6,      #'entering quantity of groceries in to stock'
         "apple": 6,
         "orange": 32,
         "pear": 15}

prices = {"banana": 4,     #'entering price of each groceries in to prices'
          "apple": 2,
          "orange": 1.5,
          "pear": 3}

def computeBill(food): #'creating a computebill function with food parameter'
    total = 0          #making total=0 initially
    for item in food:  #for every item in food calculate total
        tot = prices[item] * stock[item]
        print (item, tot)
        total += tot
    return total    #return total

computeBill(groceries)

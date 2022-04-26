#NOT WORKING


amount_due = 50

while amount_due > 0:
    print("Amount due: $" + str(amount_due))
    coin = int(input("Enter a coin: "))
    amount_due -= coin
    if amount_due <= 0:
        print("Change: $ ", abs(amount_due))
        amount_due = 0
    else:
        print("Amount due: $ " + str(amount_due))

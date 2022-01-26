# Establishing my inputs needed.
price = float(input("Enter the price of the item: $"))
print()
cash = float(input("Enter the amount of money received: $"))
change = cash - price
print()

# Printing the change given back.
print("The change of those two values is: $", format(change, ".2f"), sep="")
print()

# Printed remaining change for troubleshooting, will comment out.

twenties = int(change / 20)
print("Number of 20 dollar bills is: ", twenties)
change = change - (twenties * 20)
# print("Remaining change: $", format(change, ".2f"), sep="")
print()

# Logic is telling me that I will need to move away from using int.
# I may have to switch to a float to complete these calculations.

tens = int(change / 10)
print("Number of 10 dollar bills is: ", tens)
change = change - (tens * 10)
# print("Remaining change: $", format(change, ".2f"), sep="")
print()


fives = int(change / 5)
print("Number of 5 dollar bills is: ", fives)
change = change - (fives * 5)
# print("Remaining change: $", format(change, ".2f"), sep="")
print()

ones = int(change / 1)
print("Number of 1 dollar bills is: ", ones)
change = change - (ones * 1)
# print("Remaining change: $", format(change, ".2f"), sep="")
print()

quarters = int(change / .25)
print("Number of quarters is: ", quarters)
change = change - (quarters * .25)
# print("Remaining change: $", format(change, ".2f"), sep="")
print()

dimes = int(change / .10)
print("Number of dimes is: ", dimes)
change = change - (dimes * .10)
# print("Remaining change: $", format(change, ".2f"), sep="")
print()

nickels = int(change / .05)
print("Number of nickels is: ", nickels)
change = change - (nickels * .05)
# print("Remaining change: $", format(change, ".2f"), sep="")
print()

pennies = float(change / .01)
print("Number of pennies is: ", format(pennies, ".0f"))
change = change - (pennies * .01)
# print("Remaining change: $", format(change, ".2f"), sep="")
print()

# Through testing I never encountered any problems using int until...
# I made it down to a single penny, and for some reason ended up with 0.
# I changed to float and rounded to the whole number, which works.










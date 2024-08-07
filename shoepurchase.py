
#!/bin/python3

from shoes import shoes

low = shoes('AIR 1s',30)
medium = shoes('AIR FORCE 1s',120)
high = shoes("OFF WHITE", 400)

try:
	shoe_budget = float(input("Enter Your Shoes Budget : "))

except ValueError:
	exit("Please enter value")
	
for shoes in [high,medium,low]:
	shoes.buy(shoe_budget)

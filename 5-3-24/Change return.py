import math

cost = float(input('Enter cost of food: '))

payment = float(input('Enter payment: '))

change = round((payment - cost), 2)

print(change)

quarter = math.floor(change/0.25)
change = change - quarter * 0.25
dime = math.floor(change/0.1)
change = change - dime * 0.1
nickle = math.floor(change/0.05)
change = change - nickle * 0.05
penny = math.floor(change/0.01)
change = change - penny * 0.01

print('Your change is',quarter,'Quarters',dime,'Dimes',nickle,'Nickles',penny,'Pennies')

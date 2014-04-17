meal = float(raw_input("What the base cost of the meal?"))
tax = float(raw_input("What's the tax rate?"))
tip = float(raw_input("What percentage of tip will you pay?"))

tax_value = meal * tax
meal_with_tax = meal * (1 + tax)
tip_value = meal_with_tax * tip
total = meal_with_tax + tip_value

print "The base cost of your meal was ${:.2f}".format(meal)
print "You need to pay ${:.2f} for tax.".format(tax_value)
print "Tipping at a rate of {:.0f}%, you should leave ${:.2f} for a tip".format(tip * 100, tip_value)
print "The grand total of your meal is ${:.2f}.".format(total)

from optparse import OptionParser

parser = OptionParser()

parser.add_option("-f", "--first", dest="meal", help="base meal cost", type="float")
parser.add_option("-s", "--second", dest="tax", help="tax rate in percentages", type="float")
parser.add_option("-t", "--third", dest="tip", help="tip rate in percentages", type="float", default=".15")

(options, args) = parser.parse_args()

if not (options.meal and options.tax):
	parser.error("You need to supply an argument for -f and -s")

tax_value = options.meal * options.tax
meal_with_tax = options.meal * (1 + options.tax)
tip_value = meal_with_tax * options.tip
total = meal_with_tax + tip_value

print "The base cost of your meal was ${0:.2f}".format(options.meal)
print "You need to pay ${0:.2f} for tax.".format(tax_value)
print "Tipping at a rate of {0}%, you should leave ${1:.2f} for a tip".format(int(options.tip * 100), tip_value)
print "The grand total of your meal is ${0:.2f}.".format(total)

# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricexcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards).
# Hint: you may want to use fabricyards, which you just wrote!

import math
def fabricyards(inches):
	# Your code goes here...

	if inches> 36: 
		yard  = inches/36
		yards = math.ceil(yard)
		return yards
	elif 0<inches<=36:
		return 1
	else:
		return 0


def fabricexcess(inches):
	# Your code goes here...
	if inches>36: 
		yard  = inches%36
		if yard>0:
		
			yards = 36-yard
		
			return yards
		else:
			return 0

	elif 0<inches<36:
		a = 36-inches
		return a
	else:
		return 0
inches = 72
print(fabricexcess(inches))

	
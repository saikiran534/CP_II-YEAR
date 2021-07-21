# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs

import math
def fun_eggcartons(eggs):
	if 0<eggs<=12:
		return 1
	
	else:
		a = eggs/12
		b = math.ceil(a)
		return b

eggs = 13
print(fun_eggcartons(eggs))

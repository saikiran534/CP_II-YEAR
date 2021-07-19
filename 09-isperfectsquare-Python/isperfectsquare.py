# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

def isperfectsquare(n):
	
	if type(n)==int:
		if n>=0:
			s = n**0.5
			if (s*s==float(n)):
				return True
		else:
			return False
	else:
		return False
	# your code goes here


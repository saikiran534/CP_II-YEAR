# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	n = abs(n)
	x = [int (a) for a in str(n)]
	if len(x)>2:
		for a  in range (0,len(x)):
		
			if x[a]==x[a+1] :

				return True
	
		return False
	else:
		return False
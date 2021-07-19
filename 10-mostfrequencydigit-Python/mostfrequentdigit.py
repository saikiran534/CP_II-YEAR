# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	count = 0 

	n = [int (a) for a in str(n)]
	n.sort()
	num = n[0]
	l =[]
	for i in n:
		counter = n.count(i)
		
		if counter>count:
			count = counter
			num = i
		l.append(i)
		
		
	return num
n=5231123123123
print(mostfrequentdigit(n))
		
	

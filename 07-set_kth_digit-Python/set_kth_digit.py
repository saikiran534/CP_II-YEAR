# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	print(n)
	x = [int (a) for a in str(n)] #[4,6,8]
	print(x)
	if n<0:
		if(k>(len(x)-1)):
			return (int(f"{d}{x[0]}{x[1]}{x[2]}"))
	elif (k>(len(x)-1)):

		return(int(f"{d}{x[0]}{x[1]}{x[2]}"))
	# else:



	# a = x[-k:]
	# b=[]
	
	# b.append(int(f"{a[0]}{a[1]}"))

	# print (b[0])

n = -468
k = 3
d = 1
print(fun_set_kth_digit(n, k, d))


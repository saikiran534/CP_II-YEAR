# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	digit=abs(digit)

	x = [int (a) for a in str(digit)]
	x = x[::-1]
	if len(x)>k:
		a = x[k]
		return a
	else:
		return 0
digit = 789
k = 0
print(fun_get_kth_digit(digit,k))

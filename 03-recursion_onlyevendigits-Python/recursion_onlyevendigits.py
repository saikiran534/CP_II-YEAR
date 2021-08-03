# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def getEven(n,i=0,x=0): 
	if n == 0 : 
		return x
	else: 
		remove = n%10
		if remove%2 ==0:
			x = x+remove*(10**(i))
			i=i+1
		return getEven(n//10, i, x) 


def onlyeven(l,r=[]): 
	if(l==[]): 
		return r
	else: 
		r.append(getEven(l[0]))
		return onlyeven(l[1:],r)
def fun_recursion_onlyevendigits(l): 
	if (l ==[]): 
		return []
	return onlyeven(l,[])

	

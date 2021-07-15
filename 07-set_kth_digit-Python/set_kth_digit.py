# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):


	if n<0:
		n = abs(n)
		
		x = [int (a) for a in str(n)] 
		k=[str(i)for i in x]
		m="".join(k)
		d = str(d)
		m = d+m
		
		return (-int(m))
	
	
	x = [int (a) for a in str(n)]
	if (len(x)-1)<k:
		k=[str(i)for i in x]
		a="".join(k)
		d=str(d)
		a=d+a
		return (int(a))
	else:
		 
		a=x[::-1]
		a[k]=d
		a=a[::-1]
		k=[str(i)for i in a]

		v= "".join(k)
		return int(v)
	

	# else:
	# a = x[-k:]
	# b=[]
	# b.append(int(f"{a[0]}{a[1]}"))
	# print (b[0])

n = -468
k = 3
d = 1
print(fun_set_kth_digit(n, k, d))


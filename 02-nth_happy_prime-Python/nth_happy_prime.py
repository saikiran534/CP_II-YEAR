# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def square(n):
	sum = 0
	while(n>0):
		sum = sum+(n%10)*(n%10)
		n //=10

	return sum
def isPrime(n):
    if n <= 1:
        return False
  
   
    for i in range(2, n):
        if n % i == 0:
            return False
  
    return True


def happynumber(n):
	if n<0:
		return False
	for i in range(200):
		n = square(n)
		if n==1: 
			return True
	return (n==1)

	

def fun_nth_happy_prime(n):
	p,q=0,0
	while p<=n:
		q+=1
		if (happynumber(q)and isPrime(q)):
			p+=1
	
	return q
	
n = 4
print(fun_nth_happy_prime(n))
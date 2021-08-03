# Write the function fun_nth_palindromic_prime(n) that takes 
# a non-negative int n and returns the nth palindromic Prime, 
# which is a palidrome number such that 
# it is also a prime. 

# For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) 
# returns 2

import math


def isPrime(n):
    if n == 2:
        return True
    elif (n < 2) or (n % 2 == 0):
        return False

    for factor in range(3, math.floor(math.sqrt(n) + 1), 2):
        if n % factor == 0:
            return False
    return True


def digitCount(n):
    if n == 0:
        return 1

    count = 0
    n = abs(n)

    while n > 0:
        count += 1
        n //= 10
    return count


def isPalindrome(n):
    numDigits = digitCount(n)

    while n > 0:
        rDigit = n % 10
        lDigit = n // (10 ** (numDigits - 1))

        if rDigit != lDigit:
            return False

        n -= (lDigit * (10 ** (numDigits - 1)))
        n //= 10
        numDigits -= 2

    return True
		
def fun_nth_palindromic_prime(n):
	found = -1
	guess = 1
	while found  < n:
		guess += 1
		if isPrime(guess) and isPalindrome(guess):
			found += 1
	return guess
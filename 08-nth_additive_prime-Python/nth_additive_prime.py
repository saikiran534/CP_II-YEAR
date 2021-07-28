# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def sum(n):
    a =0
    while (n!=0):
        a = a+n%10
        n=n//10 
    return a
    
def is_prime(n): 
    if n<=1: 
        return False
    for i in range(2,n):
        if n%i==0: 
            return False
    return True 
def additive(n):

    while (len(str(n))!=1): 
        value = sum(int(n))
        
        n= value
    if (is_prime(n)):
        return True
    return False 

    
    # if (not is_prime(n)): 
    #     return False
    # return is_prime(sum(n))
def fun_nth_additive_prime(n):
    p,q=0,0
    while p<=n:  
        q=q+1   
        if (is_prime(q) and additive(q)): 
            p=p+1
    return q
n =20

print(fun_nth_additive_prime(n))
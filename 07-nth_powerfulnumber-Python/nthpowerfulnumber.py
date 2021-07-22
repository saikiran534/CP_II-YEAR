# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import math
def isPowerful(n):
    power = []
    res=n

    while n % 2 == 0:
        power.append(2)
        n = n / 2
        
  
    for i in range(3,int(math.sqrt(n))+1,2):

        while n % i== 0:
            power.append(i),
            n = n / i
            
    
    if n > 2:
        print (n)
    num= set(power)
    ber=list(num)
    
    for i in range (len(ber)):
        
        if ((res%ber[i])==0 and (res%(ber[i]**2))==0):
            
            return True
        
    return False

i=1
count = 1
n = 10
while(True):
    if(n==0):
        print(1) 
    else:
        a = isPowerful(i)
        if (a==True):
            print(i,a)
            count = count+1
    if (count == n):
        print(i)
        break
    i = i+1






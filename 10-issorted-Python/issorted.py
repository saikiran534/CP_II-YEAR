# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
    i=1
    flag=0
    while len(a)>i:
        if(a[i] < a[i - 1] ):
            flag = 1
		

        break
		
    i += 1
    # your code goes here
	
    if (not flag or len(a)==0):
        return True
	
    else:
        return False
	
a =[1,2,3,4,5]
print(issorted(a))
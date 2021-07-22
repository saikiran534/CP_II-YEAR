# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


def fun_recursions_alternatingsum(l): 
	if l ==0:
		return 0 
	else:
		a=[]
		b=[]
		for i in range(0,len(l)):
			
			if i % 2==0:
				a.append(l[i])
			else:
				b.append(l[i])
		a= sum(a)
		b=sum(b)
		c=a-b
		return c


		
		

l=[5,3,8,4]
print(fun_recursions_alternatingsum(l))
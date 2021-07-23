# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	# Your code goes here
	a.sort()
	result = []
	if a==[]:
		return -1
	else:
		for i in range(len(a)-1):
			c = a[i]-a[i+1]
			result.append(abs(c))
	return min(result)


a =[-59,-36,-13,1,-53,-92,-2,-96,-54,75]
print(smallestdifference(a))
	
# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.
import math

def median(a):
	if (len(a)==0): 
		return None
	if (len(a)%2==0): 
		c= int(len(a)/2)
	
		d = c-1
	
		e = (a[c]+a[d])/2
		return e
	else: 
		f = int(len(a)/2)
		return a[f]
	





	






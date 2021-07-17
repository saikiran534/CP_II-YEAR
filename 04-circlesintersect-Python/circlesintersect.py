# Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) 
# that takes 6 numbers (ints) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, 
# and the circle centered at (x2,y2) with radius r2, and returns True 
# if the two circles intersect and False otherwise.

def fun_circlesintersect(x1, y1, r1, x2, y2, r2):
	# your code goes here
	distance = ((x2-x1)**2+(y2-y1)**2)**0.5
	if ((r1+r2)>=distance):
		return True
	else:
		return False
	print (distance)

x1=-10
y1=8
r1=30
x2=14
y2=-24
r2=10
print(fun_circlesintersect(x1,y1,r1,x2,y2,r2))  

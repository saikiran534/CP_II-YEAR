# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	#Your code goes here
	x = [str(a) for a in str(str1)]
	y = [str (a) for a in str(str2)]
	if len(x)==len(y):
		a = len(x)
	
	# print (len(x))
	# print(x[::-1])
		if y == x[::-1]:
			return True
		else:
			return False
	else:
		return False
	
str1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str2 = "BCDEFGHIJKLMNOPQRSTUVWXYZA"
print(isrotated(str1, str2))
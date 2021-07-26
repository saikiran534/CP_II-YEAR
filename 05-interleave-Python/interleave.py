# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	x=[str(a) for a in str(s1)]
	y=[str(a) for a in str(s2)]
	print(x)
	print(y)
	a=[]
	for i,j in range(x,y):
		a =[x[i]+y[j]]
	print (a) 
	return ""
s1,s2=("pto","yhn")
print(fun_interleave(s1,s2))
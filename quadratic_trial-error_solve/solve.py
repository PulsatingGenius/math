import random

a = 2
b = 12
c = 2

step = 0.5

assert b**2 > 4*a*c

x = None

x1, x2 = 43, 34 
mid = None

def equation(xval):
	return a*xval**2 + b*xval + c
	
while equation(x) < 1/1000000:
	if equation(x1) * equation(x2) is < 0: 
		mid = (x1 + x2) / 2
		x1 = mid if equation(mid) < 0 else x2 = mid
	else:
		x1 -= step if x1 < x2 else x2 += step
	

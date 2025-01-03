# 1317. Convert Integer to the Sum of Two No-Zero Integers

def convert(number):


	a = number
	b = 0
	
	# while not (no_zero(a) and no_zero(b)):		
	# 	b += 1
	# 	a -= 1
			
	while True:
		if no_zero(a) and no_zero(b):
			break
		b += 1
		a -= 1
	return a, b



def no_zero(number):
	if '0' in str(number):
		return False
	else:
		return True






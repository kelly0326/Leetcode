# python practice updated

from l1317 import *

print("hello")

def test_no_zero():
	assert no_zero(1) == True
	assert no_zero(10) == False
	assert no_zero(-1) == True
	assert no_zero(101) == False
	assert no_zero(110) == False
	print("no zero function, all passed.")

def test_convert():
	assert convert(2) == (1, 1)
	assert convert(11) == (9, 2)
	print("convert function, all passed.")

test_no_zero() # () never needs a parameter
test_convert()
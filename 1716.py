# 1716. Calculate Money in Leetcode Bank
def calculate_saving(n_days):
	savings = 0
	for i in range(n_days):
		# print(i % 7 + 1)
		# print(i // 7)
		# print(i // 7 + i % 7 + 1)
		savings += i // 7 + i % 7 + 1
	return savings

def unit_test():
	# print(calculate_saving(20))
	assert calculate_saving(4) == 10, "calculate_saving(4) should equals 10"
	assert calculate_saving(10) == 37
	assert calculate_saving(20) == 96
	print("all test passed.")
# calculate_saving(15)
unit_test()
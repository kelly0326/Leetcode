# 1716. Calculate Money in Leetcode Bank
def calculate_saving(n_days):
	savings = 0
	for i in range(n_days):
		# print("in 5", i % 7 + 1)
		# print("in 6", i // 7)
		# print(i // 7 + i % 7 + 1)
		savings += i // 7 + i % 7 + 1
	print(savings)
	return savings
# calculate_saving(20)


def unit_test():
	assert calculate_saving(4) == 10, "calculate_saving(4) should equals 10"
	assert calculate_saving(10) == 37
	assert calculate_saving(20) == 96
	print("all test passed.")

unit_test()

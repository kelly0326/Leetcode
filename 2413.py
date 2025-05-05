class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(1, n*100):
            if i % n == 0 and i % 2 == 0:
                print(i)
                return i
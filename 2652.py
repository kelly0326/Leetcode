# Python Leetcode
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        lst = []
        for i in range(1, n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                # print(i)
                lst.append(i)
        print(lst) # 3 5 6 7
        sum = 0
        for i in range(len(lst)):
            sum = sum + lst[i]
        print(sum)
        return sum
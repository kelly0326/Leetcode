class Solution:
    def countDigits(self, num: int) -> int:
        num = str(num)
        count = 0
        for i in range(len(num)):
            print(num[i])
            if int(num) % int(num[i]) == 0:
                print('hi')
                count = count + 1
                print(count)
        return count
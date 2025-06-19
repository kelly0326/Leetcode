class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        def left_sum(nums):
            # input = [10,4,8,3]
            # output = [0,10,14,22]
            temp = []
            sum = 0
            temp.append(sum)
            for i in range(len(nums) - 1):
                sum = sum + nums[i]
               # print(sum)
                temp.append(sum)
            return temp
        left = left_sum(nums)
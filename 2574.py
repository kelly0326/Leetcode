# Python Solution
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

        def right_sum(nums):
        # input = [10,4,8,3]
        # output = [15,11,3,0]
            total = 0
            temp = []
            for i in range(len(nums)):
                total = total + nums[i]
            print(total)
            for i in range(len(nums)):
                total = total - nums[i]
                temp.append(total)
            return temp
        right = right_sum(nums)
        print(right)

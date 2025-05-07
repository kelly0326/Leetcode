class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def min_step(num):
            if num % 3 == 0:
                return 0
            elif num % 3 == 1:
                return 1
            else:
                return 1
        lst = []
        for i in range(len(nums)):
            print(nums[i], min_step(nums[i]))
            lst.append(min_step(nums[i]))
        print(lst)
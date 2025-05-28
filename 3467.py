class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            # print(nums[i])
            if nums[i] % 2 != 0:
                output.append(1)
            else:
                 output.append(0)
        print(output)
        output.sort()
        return output
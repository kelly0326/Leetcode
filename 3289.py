class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        lst = []
        duplicate = []
        for i in range(len(nums)):
            if nums[i] not in lst:
                lst.append(nums[i])
            else:
                duplicate.append(nums[i])
        print(duplicate)
        return duplicate
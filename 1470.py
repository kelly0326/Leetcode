class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # print(nums)
        lst = []
       # for i in range(len(nums)//2):
        for i in range(n):
            lst.append(nums[i])
            lst.append(nums[i + n])
        print(lst)
        return lst
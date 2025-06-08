class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        def find_smallest(array):
            smallest = array[0]
            for i in range(len(array)):
                if array[i] < smallest:
                    smallest = array[i]
            return smallest
        def find_smallest_index(array):
            # array = [4,2,1,5]
            # should return 2 as index
            smallest = find_smallest(array)
            target_index = 0
            for i in range(len(array)):
                if array[i] == smallest:
                    target_index = i
                    break  # if we find it, we don't have to go forward
            return target_index

        print(find_smallest_index([4,2,1,5]))
        def change_array_once(array, multiplier):
            # array = [4,2,1,5]
            # should return 4,2,2,5 when mul = 2
            smallest_index = find_smallest_index(array)
            array[smallest_index] = array[smallest_index] * multiplier
            return array
        print("once:", change_array_once([4,2,3,5,6], 2))

        for i in range(k):
            nums = change_array_once(nums, multiplier)
            print(nums)
        return nums
from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # print(accounts) 
        lst = []      
        for i in range(len(accounts)):
            print(accounts[i])
            print(sum(accounts[i]))
            lst.append(sum(accounts[i]))
        print(lst)
        largest = lst[0]
        for i in range(len(lst)):
            if lst[i] > largest:
                largest = lst[i]
        print(largest)
        return largest
accounts = [[1,2,3],
            [3,2,4]
                    ]
mydoor = Solution()
print(mydoor.maximumWealth(accounts))

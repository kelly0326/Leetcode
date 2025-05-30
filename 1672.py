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
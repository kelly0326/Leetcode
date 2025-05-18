class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        final_output = 0
        def test1_chac(ch):
            output = 0
            for i in range(len(stones)):
                if stones[i] == ch:
                    output = output + 1
            return output
        for i in range(len(jewels)):
            print(test1_chac(jewels[i]))
            final_output = final_output + test1_chac(jewels[i])
            print(final_output)
        return final_output
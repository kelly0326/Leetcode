class Solution:
    def defangIPaddr(self, address: str) -> str:
        output = ""
        for i in range(len(address)):
            print(address[i])
            if address[i] != '.':
                output = output + address[i]
            else:
                output = output + "[.]"
        print("output:", output)
        return output
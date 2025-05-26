class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for i in range(len(operations)):
            print(operations[i])
            if operations[i] == '++X':
                X = X + 1
            elif operations[i] == 'X++':
                X = X + 1
            elif operations[i] == '--X':
                X = X - 1
            elif operations[i] == 'X--':
                X = X - 1
        print(X)
        return X
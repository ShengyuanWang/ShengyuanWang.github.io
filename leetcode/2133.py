class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        def isValid(lst):
            n = len(lst)
            for i in range(1, n+1):
                if i not in lst:
                    return False
            return True
        n = len(matrix)
        for i in range(n):
            row = matrix[i]
            if not isValid(row):
                return False
        for i in range(n):
            column = []
            for j in range(n):
                column.append(matrix[j][i])
            if not isValid(column):
                return False

        return True





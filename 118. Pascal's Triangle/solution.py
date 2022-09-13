class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            s = []
            for j in range(i + 1):
                if j !=0 and j != i:
                    s.append(result[-1][j] + result[-1][j-1])
                else:
                    s.append(1)

            result.append(s)
        return result
            
        
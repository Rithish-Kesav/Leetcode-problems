class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n)
        count = 0
        while n:
            if n&1:
                count+=1
            n>>=1
        return count
        
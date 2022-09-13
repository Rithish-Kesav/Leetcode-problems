class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        a = x if x>y else y
        while a>0:
            if(x%2!=y%2):
                res+=1
            x,y,a = x//2, y//2, a//2
        return res
    
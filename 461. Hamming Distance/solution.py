class Solution:
    #First solution
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        a = x if x>y else y
        while a>0:
            if(x%2!=y%2):
                res+=1
            x,y,a = x//2, y//2, a//2
        return res
    
    #Second solution
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0 
        while x or y: 
            if (x&1) ^ (y&1): 
                cnt += 1 
            x >>= 1 
            y >>= 1 
        return cnt
    
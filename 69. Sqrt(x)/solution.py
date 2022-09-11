class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left+1<right:
            mid = int((left+right)/2)
            if mid*mid>x:
                right = mid
            elif mid*mid<x:
                left = mid
            elif mid*mid == x:
                return int(mid)
        if right*right == x:
            return int(right)
        return (int((left+right)/2))
        
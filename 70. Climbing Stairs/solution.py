class Solution:
    def climbStairs(self, n: int) -> int:
        # Using decision tree like method
        # Which is Memoization - Watch Neetcode video if you don't remember
        # We have used a bottom-up Dynamic Programming approach
        one, two = 1, 1
        for _ in range(n-1):
            tmp = one
            one += two
            two = tmp
        return one

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = 1
        nums.sort()
        for val in nums:
            if val == n:
                n+=1
            elif val<n:
                continue
        return n
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = Counter(nums)
        for key, val in hashMap.items():
            if val > len(nums)/2:
                return key
            else:
                continue

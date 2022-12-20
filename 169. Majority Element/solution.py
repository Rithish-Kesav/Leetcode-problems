class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = Counter(nums)
        for key, val in hashMap.items():
            if val > len(nums)/2:
                return key


# solution 2 - creating hashMap without Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        for n in nums:
            if n not in hashMap:
                hashMap[n] = 1
            else:
                hashMap[n] += 1
        for key, val in hashMap.items():
            if val > len(nums)/2:
                return key

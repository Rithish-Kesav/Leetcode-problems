class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] = hashMap[nums[i]] + 1
            else:
                hashMap[nums[i]] = 1

        for key, val in hashMap.items():
            if val == 1:
                return key

# Solution 2


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor

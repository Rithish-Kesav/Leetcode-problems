# My solution derived from Two sum
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hMap = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in hMap:
                return ([hMap[diff], i+1])
            hMap[n] = i+1
        return

# Neetcode solution


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left]+numbers[right] > target:
                right -= 1
            elif numbers[left]+numbers[right] < target:
                left += 1
            else:
                return [left+1, right+1]
                break

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

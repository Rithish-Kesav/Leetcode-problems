# Solution 1 - Very slow solution
class Solution(object):
    def containsDuplicate(self, nums):
        unique = set()
        for n in nums:
            if n in unique:
                return True
            unique.add(n)
        return False

# Solution 2 - Faster solution


class Solution(object):
    def containsDuplicate(self, nums):
        dict_nums = {}

        for i in nums:
            if i in dict_nums:
                return True
            else:
                dict_nums[i] = 1

        return False

# Solution 3 - A slower solution but faster than Solution 1


class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))

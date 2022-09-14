class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
            else:
                continue

    def missingNumber(self, nums: List[int]) -> int:
        #Not sure about logic
        allSum = (len(nums)*(len(nums)+1))/2
        arrSum = sum(nums)
        return int(allSum - arrSum)
    
    def missingNumber(self, nums: List[int]) -> int:
        #Difference of sums
        sum1 = sum(nums)
        sum2 = sum(range(len(nums)+1))
        return abs(sum2-sum1)

    def missingNumber(self, nums: List[int]) -> int:
        #Same method as before but changed logic
        ans = len(nums) 
        for i in range(len(nums)): 
            ans += i - nums[i] 
        return ans
            
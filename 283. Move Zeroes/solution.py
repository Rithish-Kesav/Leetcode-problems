class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #My solution
        
        l = 0
        for r in range(len(nums)):
            if nums[l] != 0 and nums[r] != 0:
                l+=1
            elif nums[l] == 0 and nums[r] != 0:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
            elif len(nums) == 1:
                return nums
        return nums
        
        #Secondary solution
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
        return nums
        
                
            
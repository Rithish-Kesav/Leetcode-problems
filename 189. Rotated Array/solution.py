class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        left,right = 0,len(nums) - 1
        while left<=right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
        print(nums)
        left, right = 0, k-1
        while left<=right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
        print(nums)
        left, right = k, len(nums)-1
        while left<=right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
        print(nums)
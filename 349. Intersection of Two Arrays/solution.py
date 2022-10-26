class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final = []
        blank = []
        for ele in nums1:
            if ele in nums2:
                final.append(ele)
        for val in final:
            if val not in blank:
                blank.append(val)
        return blank

# Solution 2 - Much faster


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        final = []
        for val in set1:
            if val in set2:
                final.append(val)
        return final

# Solution 1
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1) > len(nums2):
            mini = len(nums2)
            miniList, maxiList = nums2, nums1
        else:
            mini = len(nums1)
            miniList, maxiList = nums1, nums2
        for ele in miniList:
            if ele in maxiList:
                maxiList.remove(ele)
                res.append(ele)
            else:
                continue
        return res

# Solution 2


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        res = []
        for n in nums2:
            if c[n] > 0:
                res.append(n)
                c[n] -= 1
        return res

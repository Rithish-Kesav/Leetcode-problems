# My solution
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for ele in sorted(nums):
            if ele in hashMap:
                hashMap[ele] += 1
            else:
                hashMap[ele] = 1
        final = []
        hashMap = dict(sorted(hashMap.items(), key=lambda item: item[1]))
        for key, val in hashMap.items():
            final.append(key)
        return final[-k:]

# Faster solution


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        mp = {}
        for i in nums:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1

        maxHeap = [(-val, key) for key, val in mp.items()]
        heapq.heapify(maxHeap)

        while k != 0:
            x, y = heapq.heappop(maxHeap)
            ans.append(y)
            k -= 1

        return ans

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = []
        left = 0
        right = 1
        while right < len(prices):
            if (prices[right] > prices[left]):
                diff.append(prices[right]-prices[left])
            else:
                left = right
            right += 1
        if diff:
            return max(diff)
        else:
            return 0

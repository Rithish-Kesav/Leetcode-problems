class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = []
        left = 0
        right = 1
        while right < len(prices):
            if (prices[right] > prices[left]):
                diff.append(prices[right]-prices[left])
            left += 1
            right += 1
        if diff:
            return sum(diff)
        else:
            return 0

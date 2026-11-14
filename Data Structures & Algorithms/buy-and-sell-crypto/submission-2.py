class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        current_profit = max_profit = 0

        for right in range(1, len(prices)):
                current_profit = prices[right] - prices[left]
                max_profit = max(current_profit, max_profit)
                while prices[left] > prices[right]:
                    current_profit = prices[right] - prices[left]
                    max_profit = max(current_profit, max_profit)
                    left += 1
                    
        return max_profit
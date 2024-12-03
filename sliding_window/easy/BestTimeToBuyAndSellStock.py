class Solution:
    def maxProfit(self, prices):
        left = 0
        max_profit = 0
        right = 1
        while left < right and right < len(prices):
            if prices[right] > prices[left]:
                max_profit = max(max_profit,prices[right] - prices[left])
                right += 1
            else:
                left = right
                right += 1
        return max_profit
  
x = Solution()
prices = [7,1,5,3,6,4]
print(x.maxProfit(prices))
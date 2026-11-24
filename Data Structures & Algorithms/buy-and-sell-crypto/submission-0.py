class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy_index = 0
        sell_index = 1
        res = 0
        while sell_index < len(prices):
            if prices[buy_index] > prices[sell_index]:
                buy_index = sell_index
            else: 
                res = max(res, prices[sell_index] - prices[buy_index])
            sell_index += 1 
        return res
            
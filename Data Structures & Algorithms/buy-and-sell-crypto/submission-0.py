class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = prices[0]
        i = 1
        big = 0
        while i < len(prices):
            if prices[i] < curr:
                curr = prices[i]
            else:
                if prices[i] - curr > big:
                    big = prices[i] - curr
            i+=1
        return big
        
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #  solution O(n) and memory O(1)
        
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(current_profit, max_profit)
            else:
                left = right
            
            right += 1
            

        return max_profit
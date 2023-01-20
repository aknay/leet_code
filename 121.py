from typing import List


# Title: 121. Best Time to Buy and Sell Stock
# Solution Ref: Official: Approach 2: One Pass

##### start of solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # we need to set it to max so that we can compare with current price and set it to lowest
        max_profit = 0
        for i in range(len(prices)):
            current_price = prices[i]
            if current_price < min_price:
                min_price = current_price  # update to min price
            elif current_price - min_price > max_profit:  # if we found max profit, update max profit
                max_profit = current_price - min_price
        return max_profit
        # ----- Personal Note -----
        # I think this problem is more like a two pointers problem - to keep track of min price and max profit. This problem is also time series, so we can
        # just loop it through and update the min price and max profit one by one.


##### end of solution

#### test

#### case 1
s = Solution()
prices = [7, 1, 5, 3, 6, 4]
result = s.maxProfit(prices)
assert result == 5

#### case 2
s = Solution()
prices = [7, 6, 4, 3, 1]
result = s.maxProfit(prices)
assert result == 0

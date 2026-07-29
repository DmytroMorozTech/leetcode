from typing import List

# Greedy approach: since there's no limit on the number of transactions and no
# cooldown/fee, the maximum profit is just the sum of every price increase
# from one day to the next. Buying right before each uphill move and selling
# right after it captures the same total profit as any more complex sequence
# of buy/sell points, so there's no need to track "when did I buy" explicitly.
#
# Efficient because it's a single pass over the array: O(n) time, O(1) space.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit

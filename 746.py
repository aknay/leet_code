from typing import List


# Title: 746. Min Cost Climbing Stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # return min(self._min_cost_climbing_staris_r(cost, len(cost) - 1), self._min_cost_climbing_staris_r(cost, len(cost) - 2))
        return self._min_cost_climbing_staris_dp(cost)

    def _min_cost_climbing_staris_r(self, cost: List[int], index):
        # mincost(i) = cost[i]+min(mincost(i-1), mincost(i-2))
        # Base cases:
        # mincost(0) = cost[0]
        # mincost(1) = cost[1]

        if index <= 1:
            return cost[index]
        return cost[index] + min(self._min_cost_climbing_staris_r(cost, index - 1), self._min_cost_climbing_staris_r(cost, index - 2))

    def _min_cost_climbing_staris_dp(self, cost: List[int]):
        result = [cost[0], cost[1]]  # initialize non changing part
        length = len(cost)
        for i in range(2, length):  # look like if integer n, choose n + 1. if array, choose length
            result.append(cost[i] + min(result[i - 1], result[i - 2]))  # apply recursive pattern
        return min(result[length - 1], result[length - 2])


#### test

#### case 1
s = Solution()
cost = [10, 15, 20]
result = s.minCostClimbingStairs(cost)
assert result == 15

#### case 2
s = Solution()
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
result = s.minCostClimbingStairs(cost)
assert result == 6

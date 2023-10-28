class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        dp = [0] * (len(cost))
        for i in range(len(dp)):
            # i == 0 or 1,是开始选择造成的花费
            if i == 0:
                dp[0] = cost[0]
                continue

            if i == 1:
                dp[1] = cost[1]
                continue

            dp[i] = min(dp[i-2] + cost[i], dp[i-1] + cost[i])
        return dp[-1]

if __name__ == '__main__':
    cost = [10,15,20]
    solution = Solution()
    solution.minCostClimbingStairs(cost)

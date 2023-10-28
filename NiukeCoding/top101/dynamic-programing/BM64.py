# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param cost int整型一维数组
# @return int整型
#
class Solution:
    def minCostClimbingStairs(self, cost):
        # write code here
        if len(cost) == 1:
            return 0
        if len(cost) == 2:
            return min(cost[0], cost[1])

        dp = [0] * (len(cost) + 1)
        dp[2] = min(cost[0], cost[1])
        for i in range(len(cost) + 1):
            if i <= 2:
                continue
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]

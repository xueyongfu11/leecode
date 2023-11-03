
#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param prices int整型一维数组 
# @return int整型
#
class Solution:
    def maxProfit(self , prices ):
        # write code here
        dp = [[0] * 2 for _ in range(len(prices))]

        for i in range(len(prices)):
            if i == 0:
                dp[i][0] = -prices[i]
                dp[i][1] = 0
                continue
            dp[i][0] = max(-prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1])
        return dp[i][1]

s = Solution()
print(s.maxProfit([8,9,2,5,4,7,1]))


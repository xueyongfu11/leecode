

#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
class Solution:
    def rob(self , nums ):
        # write code here
        dp = [0] *  len(nums)

        for i, value in enumerate(nums):
            if i == 0:
                dp[i] = value
            elif i == 1:
                dp[i] = max(value, dp[0])
            else:
                dp[i] = max(dp[i-2] + value, dp[i-1])
        return dp[-1]



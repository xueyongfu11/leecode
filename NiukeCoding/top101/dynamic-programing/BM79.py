

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
        dp = [0] * len(nums)

        for i in range(0, len(nums)-1):
            value = nums[i]
            if i == 0:
                dp[i] = value
            elif i == 1:
                dp[i] = dp[i-1]
            else:
                dp[i] = max(dp[i-2] + value, dp[i-1])
        max_value = dp[-2]

        for i in range(0, len(nums)):
            value = nums[i]
            if i == 0:
                dp[i] = 0
            elif i == 1:
                dp[i] = nums[i]
            else:
                dp[i] = max(dp[i-2] + value, dp[i-1])
        return max(max_value,  dp[-1])

s = Solution()
print(s.rob([19,43,94,4,34,33,91,75,38,79]))
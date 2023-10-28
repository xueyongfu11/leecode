# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n in [1, 2]:
            return 1

        dp = [0] * n
        dp[0] = 1
        dp[1] = 1

        for i in range(n):
            if i in [0, 1]:
                continue
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]


# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1

        dp = [1] * number
        dp[1] = 2

        for i in range(number):
            if i in [0, 1]:
                continue
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]



#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 最少货币数
# @param arr int整型一维数组 the array
# @param aim int整型 the target
# @return int整型
#
class Solution:
    def minMoney(self , arr , aim ):
        # write code here
        if not arr:
            return -1
        if aim == 0:
            return 0

        dp = [0] * (aim + 1)
        for i in range(1, aim+1):
            min_nums = []
            for v in arr:
                if (abs(i-v) <= aim and dp[i-v] == -1) or i - v < 0:
                    pass
                else:
                    min_nums.append(dp[i-v] + 1)

            if min_nums:
                dp[i] = min(min_nums)
            else:
                dp[i] = -1
        return dp[-1]
                    

s = Solution()
print(s.minMoney([474,83,404,3],264))  # 4
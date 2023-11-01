#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 给定数组的最长严格上升子序列的长度。
# @param arr int整型一维数组 给定的数组
# @return int整型
#
class Solution:
    def LIS(self , arr ):
        # write code here
        if not arr:
            return 0
        dp = [1] * len(arr)
        for i, value in enumerate(arr):
            if i == 0: continue
            for j in range(0, i):
                if value > arr[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

s = Solution()
print(s.LIS([6,3,1,5,2,3,7]))

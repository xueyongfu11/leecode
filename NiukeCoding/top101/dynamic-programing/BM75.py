# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str1 string字符串
# @param str2 string字符串
# @return int整型
#
class Solution:
    def editDistance(self, str1, str2):
        # write code here
        dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        for i in range(len(str2) + 1):
            dp[0][i] = i
        for j in range(len(str1) + 1):
            dp[j][0] = j

        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[len(str1)][len(str2)]

s = Solution()
print(s.editDistance("nowcoder","new"))


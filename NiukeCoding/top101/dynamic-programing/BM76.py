#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param str string字符串 
# @param pattern string字符串 
# @return bool布尔型
#
class Solution:
    def match(self , str , pattern ):
        # write code here
        dp = [[False] * (len(pattern) + 1) for _ in range((len(str) + 1))]
        dp[0][0] = True

        for i in range(2, len(pattern) + 1):
            if pattern[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]

        for i in range(1, len(str) + 1):
            for j in range(1, len(pattern) + 1):  # j == 0是都是False
                if pattern[j-1] != '*' and (pattern[j-1] == '.' or pattern[j-1] == str[i-1]):
                    dp[i][j] = dp[i-1][j-1]
                elif pattern[j-1] == '*' and j >= 2:
                    if pattern[j-2] == '.' or pattern[j-2] == str[i-1]:  # *的前一位和str的当前位相等
                        dp[i][j] = dp[i][j-2] or dp[i-1][j] # 两种情况： *表示0时；*表示1至多个时
                    else:    # *的前一位和str的当前位不相等
                        dp[i][j] = dp[i][j-2]  # 只有一种情况：*表示0
        return dp[len(str)][len(pattern)]





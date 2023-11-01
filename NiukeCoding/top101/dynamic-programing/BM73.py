#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param A string字符串 
# @return int整型
#
class Solution:
    def getLongestPalindrome(self , A ):
        # write code here
        dp = [[False] * len(A) for _ in range(len(A))]
        max_len = 0

        for l in range(0, len(A)):
            for i in range(0, len(A) - l):
                j = i + l
                if l == 0:
                    dp[i][j] = True
                elif A[i] == A[j]:
                    dp[i][j] = dp[i+1][j-1]
                
                if dp[i][j]:
                    max_len = l + 1
        return max_len

s = Solution()
print(s.getLongestPalindrome("baabccc"))

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common subsequence
# @param s1 string字符串 the string
# @param s2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self, s1: str, s2: str) -> str:
        # write code here
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for i in range(len(s1)):
            for j in range(len(s2)):
                char1 = s1[i]
                char2 = s2[j]
                if char1 == char2:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        pub_substr = ''
        m, n = len(s1), len(s2)
        while m >= 1 and n >= 1:
            if s1[m-1] == s2[n-1]:
                pub_substr += s1[m-1]
                m -= 1
                n -= 1
            elif dp[m][n - 1] > dp[m - 1][n]:
                n -= 1
            else:
                m -= 1
        if pub_substr == '':
            return '-1'
        else:
            return pub_substr[::-1]


if __name__ == '__main__':
    solution = Solution()
    res = solution.LCS("1A2C3D4B56", "B1D23A456A")
    print(res)

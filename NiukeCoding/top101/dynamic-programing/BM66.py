#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self, str1: str, str2: str) -> str:
        # write code here
        dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

        max_v = -100
        max_index = None

        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    if dp[i + 1][j + 1] > max_v:
                        max_v = dp[i + 1][j + 1]
                        max_index = i

        if max_v < 0:
            return '-1'
        else:
            return str1[max_index - max_v + 1:max_index + 1]


if __name__ == '__main__':
    solution = Solution()
    res = solution.LCS("1A222C3D4B56", "B1D2223A456A")
    print(res)

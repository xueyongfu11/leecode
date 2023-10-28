#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param matrix int整型二维数组 the matrix
# @return int整型
#
class Solution:
    def minPathSum(self, matrix):
        # write code here
        li = matrix
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(n):
            if i == 0:
                dp[0][i] = li[0][i]
            else:
                dp[0][i] = dp[0][i - 1] + li[0][i]
        for i in range(m):
            if i == 0:
                dp[i][0] = li[i][0]
            else:
                dp[i][0] = dp[i - 1][0] + li[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + li[i][j]

        return dp[m - 1][n - 1]


if __name__ == '__main__':
    solution = Solution()
    li = [[1, 3, 5, 9], [8, 1, 3, 4], [5, 0, 6, 1], [8, 8, 4, 0]]
    res = solution.minPathSum(li)
    print(res)

# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 递增路径的最大长度
# @param matrix int整型二维数组 描述矩阵的每个数
# @return int整型
#
class Solution:
    def solve(self, matrix):
        # write code here
        n = len(matrix)
        m = len(matrix[0])

        mat = [[-1] * m for _ in range(n)]
        self.func(n, m, 0, 0, mat)

        return max([max(li) for li in mat])

    def func(self, n, m, i, j, mat):
        if mat[i][j] != -1:
            return mat[i][j]

        max_v = 0
        if self.is_valid(n, m, i, j + 1, mat, mat[i][j]):
            mat[i][j+1] = 0
            max_v = max(self.func(n, m, i, j + 1, mat), max_v)
            mat[i][j+1] = -1

        if self.is_valid(n, m, i, j - 1, mat, mat[i][j]):
            mat[i][j-1] = 0
            max_v = max(self.func(n, m, i, j - 1, mat), max_v)
            mat[i][j-1] = -1

        if self.is_valid(n, m, i + 1, j, mat, mat[i][j]):
            mat[i+1][j] = 0
            max_v = max(self.func(n, m, i + 1, j, mat), max_v)
            mat[i+1][j] = -1

        if self.is_valid(n, m, i - 1, j, mat, mat[i][j]):
            mat[i - 1][j] = 0
            max_v = max(self.func(n, m, i - 1, j, mat), max_v)
            mat[i - 1][j] = -1

        mat[i][j] = max_v + 1
        return max_v + 1

    def is_valid(self, n, m, i, j, mat, last_value):
        # 越界、数值非递增
        if i == n or j == m or mat[i][j] > last_value:
            return False
        return True

s = Solution()
print(s.solve([[1,2,3],[4,5,6],[7,8,9]]))
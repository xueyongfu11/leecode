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
        for i in range(n):
            for j in range(m):
                self.func(n, m, i, j, mat, matrix)

        return max([max(li) for li in mat])

    def func(self, n, m, i, j, mat, matrix):
        if mat[i][j] != -1:
            return mat[i][j]

        max_v = 0
        if self.is_valid(n, m, i, j + 1, matrix, matrix[i][j]):
            max_v = max(self.func(n, m, i, j + 1, mat, matrix), max_v)

        if self.is_valid(n, m, i, j - 1, matrix, matrix[i][j]):
            max_v = max(self.func(n, m, i, j - 1, mat, matrix), max_v)

        if self.is_valid(n, m, i + 1, j, matrix, matrix[i][j]):
            max_v = max(self.func(n, m, i + 1, j, mat, matrix), max_v)

        if self.is_valid(n, m, i - 1, j, matrix, matrix[i][j]):
            max_v = max(self.func(n, m, i - 1, j, mat, matrix), max_v)

        mat[i][j] = max_v + 1
        return max_v + 1

    def is_valid(self, n, m, i, j, matrix, last_value):
        if i == n or j == m or i < 0 or j < 0 or matrix[i][j] <= last_value:
            return False
        return True

s = Solution()
print(s.solve([[4,3,3,6,6,3,2,1,0,7],
[1,8,2,8,5,9,2,8,3,1],[8,0,9,2,4,3,2,4,3,7],[1,2,2,6,3,0,3,9,7,0],
[7,4,3,8,8,3,2,4,6,8],[2,8,9,2,9,3,0,8,7,8],[8,9,9,4,6,3,3,4,9,6],
[2,8,3,8,1,3,7,3,0,7],[2,1,1,6,4,1,0,8,1,6],[4,1,3,6,3,4,4,4,0,3]]))



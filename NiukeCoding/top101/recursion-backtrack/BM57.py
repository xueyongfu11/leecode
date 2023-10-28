#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 判断岛屿数量
# @param grid char字符型二维数组
# @return int整型
#
class Solution:
    def solve(self , grid ):
        # write code here
        num = 0
        row_n = len(grid)
        col_n = len(grid[0])
        for i in range(row_n):
            for j in range(col_n):
                if grid[i][j] == '1':
                    num += 1
                    self.func(grid, i, j, row_n, col_n)
        return num


    def func(self, grid, i, j, row_n, col_n):
        if grid[i][j] == '1':
            grid[i][j] = '0'
            if i - 1 >= 0:
                self.func(grid, i-1, j, row_n, col_n)
            if j - 1 >= 0:
                self.func(grid, i, j-1, row_n, col_n)
            if i + 1 < row_n:
                self.func(grid, i+1, j, row_n, col_n)
            if j + 1 < col_n:
                self.func(grid, i, j+1, row_n, col_n)

s = Solution()
print(s.solve([[1]]))
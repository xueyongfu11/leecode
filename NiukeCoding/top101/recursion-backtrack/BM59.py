# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 the n
# @return int整型
#
class Solution:

    def Nqueen(self, n):
        taken_pos = [-1] * n
        num = self.func(n, 0, taken_pos)
        return num

    def is_valid(self, row_n, col_n, taken_pos):
        for i, value in enumerate(taken_pos):
            if value != -1 and (row_n == i or col_n == value or abs(row_n - i) == abs(col_n - value)):
                return False
        return True

    def func(self, n, row_n, taken_pos):
        if row_n == n:
            return 1

        num = 0
        for col_n in range(n):
            if self.is_valid(row_n, col_n, taken_pos):
                taken_pos[row_n] = col_n
                num += self.func(n, row_n + 1, taken_pos)
                taken_pos[row_n] = -1
        return num

s = Solution()
print(s.Nqueen(4))

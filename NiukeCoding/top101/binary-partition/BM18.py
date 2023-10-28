#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param target int整型
# @param array int整型二维数组
# @return bool布尔型
#
from typing import List


class Solution:
    def Find(self, target: int, array: List[List[int]]) -> bool:
        # write code here
        row_i = len(array) - 1
        col_i = 0
        while row_i >= 0 and col_i < len(array[0]):
            value = array[row_i][col_i]
            if value == target:
                return True
            elif value > target:
                row_i -= 1
            else:
                col_i += 1

        return False


if __name__ == '__main__':
    solution = Solution()
    nums = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    target = 13
    print(solution.Find(target, nums))

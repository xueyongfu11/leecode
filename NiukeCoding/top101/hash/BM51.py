#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return int整型
#
from typing import List


class Solution:
    def MoreThanHalfNum_Solution(self, numbers: List[int]) -> int:
        # write code here
        mappings = {}
        length = len(numbers)
        for v in numbers:
            if v in mappings:
                mappings[v] += 1
            else:
                mappings[v] = 1
            if mappings[v] / length > 0.5:
                return v

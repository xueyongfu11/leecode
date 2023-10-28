#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @param target int整型
# @return int整型一维数组
#
from typing import List


class Solution:
    '''
    非最优方法：可以尝试使用一次循环，得到结果
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # write code here
        mappings = {}
        for i, num in enumerate(numbers):
            if num in mappings:
                mappings[num].append(i + 1)
            else:
                mappings[num] = [i + 1]

        for num, indexes in mappings.items():
            if target - num in mappings:
                if target - num == num:
                    if len(indexes) >= 2:
                        return indexes[:2]
                else:
                    i1 = indexes[0]
                    i2 = mappings[target - num][0]
                    if i1 > i2:
                        return [i2, i1]
                    else:
                        return [i1, i2]


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum(nums, target))

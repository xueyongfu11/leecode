

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#
from typing import List


class Solution:
    def search(self , nums: List[int], target: int) -> int:
        # write code here
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = start + int((end - start) / 2)
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
        return -1

if __name__ == '__main__':
    solution = Solution()
    nums = [-1,0,3,4,6,10,13,14]
    target = 13
    print(solution.search(nums, target))

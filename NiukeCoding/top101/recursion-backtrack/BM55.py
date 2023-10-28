#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @return int整型二维数组
#
from typing import List


class Solution:
    def permute(self, num: List[int]) -> List[List[int]]:
        # write code here
        num = sorted(num)
        results = []

        def recursion(li, results, i):
            # i: 当前指向的位置index，该位置已经和之前的位置交换，未和index之后的位置交换
            if i == len(li) - 1:
                results.append(li.copy())
            else:
                for j in range(i, len(li)):
                    if i == j:
                        # 不交换
                        recursion(li, results, i + 1)
                    else:
                        # 交换
                        temp = li[i]
                        li[i] = li[j]
                        li[j] = temp
                        recursion(li, results, i + 1)
                        # 交换回来
                        li[j] = li[i]
                        li[i] = temp

        recursion(num, results, 0)

        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3, 4]))

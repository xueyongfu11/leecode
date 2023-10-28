# coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @param size int整型
# @return int整型一维数组
#
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size > len(num) or size == 0:
            return

        li = []
        queue = []

        for i in range(size):
            while queue and num[queue[-1]] < num[i]:
                queue.pop()
            queue.append(i)
        li.append(num[queue[0]])

        for i in range(size, len(num)):
            # 先弹去非当前窗口的index
            while queue and queue[0] < i - size + 1:
                queue.pop(0)

            # 将当前的值加入窗口
            while queue and num[queue[-1]] < num[i]:
                queue.pop()
            queue.append(i)

            li.append(num[queue[0]])

        return li


if __name__ == '__main__':
    s = Solution()
    s.maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3)

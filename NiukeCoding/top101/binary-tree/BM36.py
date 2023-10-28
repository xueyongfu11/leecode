# coding:utf-8
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return bool布尔型
#
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if self.depth(pRoot) == -1:
            return False
        else:
            return True

    def depth(self, root):
        if not root:
            return 0

        l_depth = self.depth(root.left)
        if l_depth == -1:
            return -1

        r_depth = self.depth(root.right)
        if r_depth == -1:
            return -1

        if abs(l_depth - r_depth) > 1:
            return -1

        return max(l_depth, r_depth) + 1

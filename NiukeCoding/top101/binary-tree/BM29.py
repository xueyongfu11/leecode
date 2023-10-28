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
# @param root TreeNode类
# @param sum int整型
# @return bool布尔型
#
class Solution:
    def hasPathSum(self, root, sum):
        # write code here

        if not root:
            return False

        def func(root, res):
            if not root:
                return False

            res += root.val
            if not root.left and not root.right and res == sum:
                return True
    
            return func(root.left, res) or func(root.right, res)

        return func(root, 0)



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
    def isSymmetrical(self, pRoot):
        # write code here

        if not pRoot:
            return True

        return self.func(pRoot.left, pRoot.right)

    def func(self, root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        else:
            if root1.val == root2.val:
                return self.func(root1.left, root2.right) and \
                       self.func(root1.right, root2.left)
            else:
                return False

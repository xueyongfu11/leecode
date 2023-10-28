
#coding:utf-8
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
# @param p int整型
# @param q int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self , root , p , q ):
        # write code here
        if not root:
            return -1

        if (root.val >= p and root.val <= q) or (root.val >= q and root.val <= p):
            return root.val

        if root.val > p and root.val > q:
            return self.lowestCommonAncestor(root.left, p, q)

        if root.val < p and root.val < q:
            return self.lowestCommonAncestor(root.right, p, q)
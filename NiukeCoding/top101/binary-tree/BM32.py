
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
# @param t1 TreeNode类
# @param t2 TreeNode类
# @return TreeNode类
#
class Solution:
    def mergeTrees(self , t1 , t2 ):
        # write code here
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        elif not t1 and t2:
            t1 = t2
        return t1

#coding:utf-8
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param preOrder int整型一维数组
# @param vinOrder int整型一维数组
# @return TreeNode类
#
class Solution:
    def reConstructBinaryTree(self , preOrder , vinOrder ):
        # write code here
        if not preOrder:
            return None

        root_value = preOrder[0]
        index = vinOrder.index(root_value)
        node = TreeNode(root_value)
        node.left = self.reConstructBinaryTree(preOrder[1:1+index], vinOrder[0:index])
        node.right = self.reConstructBinaryTree(preOrder[1+index:], vinOrder[index+1:])
        return node
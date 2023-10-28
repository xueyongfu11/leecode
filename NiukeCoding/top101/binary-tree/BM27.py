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
# @return int整型二维数组
#
import copy
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []

        li = []
        stack1 = []
        stack2 = []

        stack1.append(pRoot)

        while stack1 or stack2:
            tmp = []
            while stack1:
                node = stack1.pop(-1)
                tmp.append(node.val)
                if node.left: stack2.append(node.left)
                if node.right: stack2.append(node.right)

            if tmp: li.append(copy.deepcopy(tmp))

            tmp = []
            while stack2:
                node = stack2.pop(-1)
                tmp.append(node.val)
                if node.right: stack1.append(node.right)
                if node.right: stack1.append(node.left)

            if tmp: li.append(tmp)
        return li

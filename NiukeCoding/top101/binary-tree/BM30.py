# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.root = None
        self.pre = None

    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return

        self.Convert(pRootOfTree.left)

        if self.pre is None:
            self.pre = pRootOfTree
            self.root = pRootOfTree
        else:
            self.pre.right = pRootOfTree
            pRootOfTree.left = self.pre
            self.pre = pRootOfTree

        self.Convert(pRootOfTree.right)

        return self.root
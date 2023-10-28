from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @return int整型一维数组
#
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # write code here
        li = []
        if not root:
            return li
        self.inorder(li, root)
        return li

    def inorder(self, li: List, root: TreeNode):
        if root is None:
            return
        self.inorder(li, root.left)
        li.append(root.val)
        self.inorder(li, root.right)
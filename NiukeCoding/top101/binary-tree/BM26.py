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

# class Solution:
#     def levelOrder(self , root: TreeNode) -> List[List[int]]:
#         # write code here
#         if not root:
#             return []
#         li = []
#         queue = [root]
#         self.level_order(li, queue)
#         return li
#
#     def level_order(self, li, queue):
#         if queue == []:
#             return
#         tmp = []
#         for _ in range(len(queue)):
#             node = queue.pop()
#             tmp.append(node.val)
#             if node.left:
#                 queue.insert(0, node.left)
#             if node.right:
#                 queue.insert(0, node.right)
#         li.append(tmp)
#         self.level_order(li, queue)


# 非递归方式

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
# @return int整型二维数组
#
class Solution:
    def levelOrder(self , root ):
        # write code here
        if not root:
            return []

        li = []
        queue = []
        queue.insert(0, root)

        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(-1)
                tmp.append(node.val)
                if node.left: queue.insert(0, node.left)
                if node.right: queue.insert(0, node.right)
            li.append(tmp)
        return li
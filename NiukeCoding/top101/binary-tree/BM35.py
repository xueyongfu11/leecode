
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
# @return bool布尔型
#
class Solution:
    def isCompleteTree(self , root ):
        # write code here
        if not root:
            return True

        queue = []
        queue.insert(0, root)

        flag = False
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(-1)
                if not cur:
                    flag = True
                else:
                    if flag:
                        return False
                    queue.insert(0, cur.left)
                    queue.insert(0, cur.right)
        return True
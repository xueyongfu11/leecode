
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
# @param o1 int整型
# @param o2 int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self , root , o1 , o2 ):
        # write code here
        _, _, value = self.func(root, o1, o2)
        return value

    def func(self, root, o1, o2):
        if not root:
            return False, False, None

        l_find_o1, l_find_o2, value1 = self.func(root.left, o1, o2)
        r_find_o1, r_find_o2, value2 = self.func(root.right, o1, o2)

        if value1:
            return True, True, value1
        if value2:
            return True, True, value2

        o1_flag = (root.val == o1 or l_find_o1 or r_find_o1)
        o2_flag = (root.val== o2 or l_find_o2 or r_find_o2)

        if o1_flag and o2_flag:
            return o1_flag, o2_flag, root.val

        return o1_flag, o2_flag, None


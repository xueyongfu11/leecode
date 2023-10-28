# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(root):
            if root is None:
                return 0, True

            left_deep, left_flag = dfs(root.left)
            right_deep, right_flag = dfs(root.right)
            if left_flag and right_flag:
                if abs(left_deep - right_deep) <= 1:
                    return max(left_deep, right_deep) + 1, True
                else:
                    return 0, False
            else:
                return 0, False
        _, flag = dfs(root)
        return flag










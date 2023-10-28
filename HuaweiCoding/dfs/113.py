# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(root, nums, total):
            if root is None:
                return

            total += root.val
            nums.append(root.val)

            if root.left is None and root.right is None:
                if total == targetSum:
                    res.append(nums)
                return

            dfs(root.left, nums.copy(), total)
            dfs(root.right, nums.copy(), total)

        dfs(root, [], 0)
        return res

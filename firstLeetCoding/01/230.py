# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.v = None

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def cur(root, k):
            if root:
                cur(root.left, k)
                li.append(root.val)
                if len(li) == k:
                    self.v = root.val
                cur(root.right, k)

        li = []
        cur(root, k)
        return self.v

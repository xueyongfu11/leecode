# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        def dfs(root):
            if root is None:
                return None

            if root.val > key:
                root.left = dfs(root.left)
                return root  # dfs(root.left)分支中可能没找到，会返回空，这样就相当于root.left = None
            elif root.val < key:
                root.right = dfs(root.right)
                return root
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    r_node = root.right
                    while r_node.left:
                        r_node = r_node.left
                    r_node.left = root.left
                    return root.right

        return dfs(root)

class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def recu(root):
            if root:
                recu(root.left)
                li.append(root.val)
                recu(root.right)

        li = []
        recu(root)
        return li

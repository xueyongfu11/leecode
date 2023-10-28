class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def recu(root):
            if root:
                recu(root.left)
                recu(root.right)
                li.append(root.val)

        li = []
        recu(root)
        return li

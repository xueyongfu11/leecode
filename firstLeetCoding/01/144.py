# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree(object):
    """二叉树结构"""

    def __init__(self, node=None):
        self.root = node

    def add(self, item=None):
        """添加节点，item为数值"""
        node = TreeNode(val=item)  # 建立节点
        if not self.root or self.root.val is None:  # 空树
            self.root = node
        else:
            queue = []
            queue.append(self.root)  # 通过队列来完成二叉树的构建
            while True:
                current_node = queue.pop(0)  # 当前待判断的节点
                if current_node.val is None:
                    continue
                if not current_node.left:  # 左树为空
                    current_node.left = node
                    return
                elif not current_node.right:
                    current_node.right = node
                    return
                else:  # 左右都有值，添加到queue待弹出
                    queue.append(current_node.left)
                    queue.append(current_node.right)


tree = Tree()
for i in [1, None, 2, 3]:
    tree.add(i)


class Solution(object):
    def __init__(self):
        self.li = []

    def recu(self,root):
        if root:
            self.li.append(root.val)
            self.recu(root.left)
            self.recu(root.right)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.recu(root)
        return self.li



s = Solution()
print(s.preorderTraversal(tree.root))




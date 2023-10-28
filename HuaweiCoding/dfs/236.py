class TreeNode(object):
    def __init__(self, item):
        """
        param: self.elem 是结点的数据域
                self.lchild 是结点的左孩子
                self.rchild 是结点的右孩子
        """
        self.val = item
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        """
        param: item 是传进来来的数据,我们要实例化一个结点取接收他,但是他的位置要放在树梢,不能乱插入
                queue 我们创建一个队列来接收和弹出结点,这样我们找到结点需要接收的位置
        """
        node = TreeNode(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)

            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)


tree = Tree()
li = [3,5,1,6,2,0,8,None,None,7,4]
for l in li:
    tree.add(l)
root = tree.root



class Solution(object):
    def __init__(self):
        self.res = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def dfs(root):
            if root is None:
                return 0, True

            num = 0
            if root == p:
                num += 1
            if root == q:
                num += 1

            v, flag= dfs(root.left)
            if not flag:
                return 0, False
            num += v
            if num == 2:
                self.res = root
                return 0, False

            v, flag = dfs(root.right)
            if not flag:
                return 0, False
            num += v
            if num == 2:
                self.res = root
                return 0, False

            return num, True
        dfs(root)
        return self.res










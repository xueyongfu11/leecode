# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.s = ''

    def Serialize(self, root):
        # write code here

        def func(root):
            if not root:
                self.s += '#_'
                return

            self.s += str(root.val) + '_'

            func(root.left)
            func(root.right)

        func(root)
        return self.s

    def Deserialize(self, s):
        # write code here
        values = s[:-1].split('_')
        if values[0] == '#':
            return None

        root = TreeNode(int(values.pop(0)))

        def func(root, values):
            if not values:
                return

            left_v = values.pop(0)
            if left_v != '#':
                node = TreeNode(int(left_v))
                root.left = node
                func(node, values)

            if not values:
                return

            right_v = values.pop(0)
            if right_v != '#':
                node = TreeNode(int(right_v))
                root.right = node
                func(node, values)

        func(root, values)
        return root

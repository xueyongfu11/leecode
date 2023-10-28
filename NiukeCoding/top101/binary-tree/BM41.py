from typing import List
from collections import defaultdict


class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # 建树函数
    # 四个int参数分别是前序最左节点下标，前序最右节点下标
    # 中序最左节点下标，中序最右节点坐标
    def buildTree(self, xianxu: List[int], l1: int, r1: int, zhongxu: List[int], l2: int, r2: int) -> TreeNode:
        if l1 > r1 or l2 > r2:
            return None
        # 构建节点
        root = TreeNode(xianxu[l1])
        # 用来保存根节点在中序遍历列表的下标
        rootIndex = 0
        # 寻找根节点
        for i in range(l2, r2 + 1):
            if zhongxu[i] == xianxu[l1]:
                rootIndex = i
                break
        # 左子树大小
        leftsize = rootIndex - l2
        # 右子树大小
        rightsize = r2 - rootIndex
        # 递归构建左子树和右子树
        root.left = self.buildTree(xianxu, l1 + 1, l1 + leftsize, zhongxu, l2, l2 + leftsize - 1)
        root.right = self.buildTree(xianxu, r1 - rightsize + 1, r1, zhongxu, rootIndex + 1, r2)
        return root

    def rightSideView(self, root: TreeNode):
        # 右边最深处的值
        mp = defaultdict(int)
        # 记录最大深度
        max_depth = -1
        # 维护深度访问节点和维护dfs时的深度
        nodes, depths = [], []
        nodes.append(root)
        depths.append(0)
        while nodes:
            node = nodes[-1]
            nodes.pop()
            depth = depths[-1]
            depths.pop()
            if node:
                # 维护二叉树的最大深度
                max_depth = max([max_depth, depth])
                # 如果不存在对应深度的节点我们才插入
                if mp[depth] == 0:
                    mp[depth] = node.val
                nodes.append(node.left)
                nodes.append(node.right)
                depths.append(depth + 1)
                depths.append(depth + 1)
        res = []
        for i in range(max_depth + 1):
            res.append(mp[i])
        return res

    def solve(self, xianxu: List[int], zhongxu: List[int]) -> List[int]:
        res = []
        # 空节点
        if (len(xianxu) == 0):
            return res
        # 建树
        root = self.buildTree(xianxu, 0, len(xianxu) - 1, zhongxu, 0, len(zhongxu) - 1)
        # 找每一层最右边的节点
        return self.rightSideView(root)

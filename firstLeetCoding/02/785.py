class Solution_False(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        setA = set()
        setB = set()
        for node, adjoin_node in enumerate(graph):
            if node == 0:
                setA.add(node)
                setB.update(adjoin_node)
                continue

            if not adjoin_node:
                setA.add(node)
                continue

            if node in setA:
                for ad in adjoin_node:
                    if ad in setA:
                        return False
                    else:
                        setB.add(ad)
            else:
                for ad in adjoin_node:
                    if ad in setB:
                        return False
                    else:
                        setA.add(ad)
        return True


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        state = [0] * n
        verify = True
        def dfs(i, state, cor):
            nonlocal verify

            if state[i] == 0:
                state[i] = cor
            else:
                if state[i] != cor:
                    verify = False
                return

            adjoin_cor = 1 if state[i] == 2 else 2

            for nei in graph[i]:
                dfs(nei, state, adjoin_cor)

        for i in range(n):
            if state[i] == 0:
                dfs(i, state, 1)

        return verify


s = Solution()
graph = [[4], [], [4], [4], [0, 2, 3]]
print(s.isBipartite(graph))

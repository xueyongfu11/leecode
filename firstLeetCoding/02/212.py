import collections
import copy


class Trie:
    def __init__(self, word=''):
        self.word = word
        self.children = collections.defaultdict(Trie)

    def add(self, word, trie):
        cur = trie
        for char in word:
            cur = cur.children[char]
        cur.word = word


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.add(word, trie)

        def dfs(now, i, j):
            if board[i][j] not in now.children:
                return

            ch = board[i][j]
            nex = now.children[ch]

            if nex.word != '':
                ans.add(nex.word)

            board[i][j] = '#'
            for i2, j2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= i2 < m and 0 <= j2 < n:
                    dfs(nex, i2, j2)
            board[i][j] = ch

        ans = set()
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return ans


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
s = Solution()
res = s.findWords(board, words)
print(res)


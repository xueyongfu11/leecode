class Solution:
    def totalNQueens(self, n: int) -> int:

        def backtrack(x, y, off, points_y, total):
            off = off.copy()
            points_y = points_y.copy()
            points_y.add(y)

            if (x == n - 1) and ((x, y) not in off):
                total.append(1)
                return

            for i in range(n - x):
                if (y + i) <= n:
                    off.add((x + i, y + i))
                if (y - i) >= 0:
                    off.add((x + i, y - i))

            for x1 in range(x + 1, n):
                flag = False
                # 如果一行未放，那么points_y的数量小于x1
                if (x1 > len(points_y)):
                    return
                for y1 in range(0, n):

                    if (y1 in points_y) or ((x1, y1) in off):
                        continue

                    flag = True

                    # x1, y1可以放
                    backtrack(x1, y1, off, points_y, total)
                if not flag:
                    return

        t = 0
        for i in range(n):
            total = []
            backtrack(0, i, set(), set(), total)
            t += sum(total)
        return t


class Solution2:
    def totalNQueens(self, n: int) -> int:

        def backtrack(row: int) -> int:
            if row == n:
                return 1
            else:
                count = 0
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    count += backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)
                return count

        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        return backtrack(0)


if __name__ == '__main__':
    solution = Solution2()
    n = 50
    res = solution.totalNQueens(n)
    print(res)

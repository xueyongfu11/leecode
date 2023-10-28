class Solution1:
    def combinationSum(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        res = []

        def helper(i, tmp_sum, tmp):
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            helper(i, tmp_sum + candidates[i], tmp + [candidates[i]])
            helper(i + 1, tmp_sum, tmp)

        helper(0, 0, [])
        return res


class Solution2:
    def combinationSum(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i, tmp_sum, tmp):
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                backtrack(j, tmp_sum + candidates[j], tmp + [candidates[j]])

        backtrack(0, 0, [])
        return res


class Solution3:
    def combinationSum(self, candidates, target):
        if len(candidates) == 0:
            return []
        candidates.sort()
        path = []
        res = []
        '''
        ！！！重点！！！
        在python中，如果传参是mutable var, 那么传参相当于引用，因此调用后，如果调用函数的内部对该传入变量进行修改，就会导致直接改变原始对象。这就是典型的privacy leak！！发生了。
        例如在这个，list就是该mutable var，而如果以path或res 为传参，放在__DFS 中， 那么就相当于在__DFS内部，实际上用的都是一个物理地址下的res和path，类似于全局变量。
        因此combinationSum下的局部变量path和res也在——DFS运行的过程中发生了改变。

        利用这个性质，我们可以把mutable var当成传入参数，从而实现全局变量的效果。
        '''
        self.__DFS(candidates, target, 0, path, res)
        return res

    '''
        DFS的实现
    '''

    def __DFS(self, candidates, target, begin, path, res):
        path = path.copy()
        # 递归出口 就是余数为0
        if target == 0:
            res.append(path)  # 记录该符合条件的结果
            return

        # 若当前路径有可能可行。
        for i in range(begin, len(candidates)):  # 我们现在到begin的节点上了
            if target - candidates[i] < 0:  # 剪枝条件
                return  # 如果当前节点就不行了，就不用继续了,这里到不用继续了即包括该depth不用继续了，也包括该节点更大到child也不用继续了，该节点pop出来

            path.append(candidates[i])  # 记录当前为止
            self.__DFS(candidates, target - candidates[i], i, path, res)  # 向下继续走，记住递归不是return，递归到实现是调用！一旦return发生，递归停止。
            path.pop()  # 回朔清理。当前节点下的所有情况都进行完了，该节点也不应该在path里面了。


class Solution:
    def combinationSum(self, candidates, target):
        res = []
        n = len(candidates)
        candidates.sort()

        def backtrack(i, tmp, res):
            tmp = tmp.copy()
            tmp_sum = sum(tmp)
            if tmp_sum == target:
                res.append(tmp)
            if tmp_sum > target:
                return

            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    return  # 跳出循环即可，因为candidate是排好序的
                tmp.append(candidates[j])
                backtrack(j, tmp, res)
                tmp.pop()

        backtrack(0, [], res)
        return res


if __name__ == '__main__':
    solution = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    res = solution.combinationSum(candidates, target)
    print(res)

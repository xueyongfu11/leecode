import collections


class Solution:
    def topKFrequent(self, nums, k: int):
        def sift_down(arr, root, k):
            """下沉log(k),如果新的根节点>子节点就一直下沉"""
            val = arr[root]  # 用类似插入排序的赋值交换
            while root << 1 < k:
                child = root << 1
                # 选取左右孩子中小的与父节点交换
                if child | 1 < k and arr[child | 1][1] < arr[child][1]:
                    child |= 1
                # 如果子节点<新节点,交换,如果已经有序break
                if arr[child][1] < val[1]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = val

        def sift_up(arr, child):
            """上浮log(k),如果新加入的节点<父节点就一直上浮"""
            val = arr[child]
            # child >> 1 > 0用来判断是否有父节点，尾部节点的值和其父节点的值比较
            while child >> 1 > 0 and val[1] < arr[child >> 1][1]:
                # 父节点的值较大，就让子节点上浮，将父节点的值赋值给子节点
                arr[child] = arr[child >> 1]
                # child的索引为父节点的索引
                child >>= 1

            arr[child] = val

        stat = collections.Counter(nums)
        stat = list(stat.items())
        heap = [(0, 0)]

        # 构建规模为k+1的堆,新元素加入堆尾,上浮
        for i in range(k):
            heap.append(stat[i])
            sift_up(heap, len(heap) - 1)
        # 维护规模为k+1的堆,如果新元素大于堆顶,入堆,并下沉
        for i in range(k, len(stat)):
            if stat[i][1] > heap[1][1]:
                heap[1] = stat[i]
                sift_down(heap, 1, k + 1)
        return [item[0] for item in heap[1:]]


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))


def heapSort(arr):
    def sift_down(arr, root, k):
        val = arr[root]
        while root << 1 < k:
            chlid = root << 1
            if chlid | 1 < k and arr[chlid | 1] > arr[chlid]:
                chlid |= 1
            if arr[chlid] > val:
                arr[root] = arr[chlid]
                root = chlid
            else:
                break
        arr[root] = val

    arr = [0] + arr
    k = len(arr)
    for i in range((k - 1) >> 1, 0, -1):
        sift_down(arr, i, k)
    for i in range(k - 1, 0, -1):
        arr[1], arr[i] = arr[i], arr[1]
        sift_down(arr, 1, i)
    return arr[1:]

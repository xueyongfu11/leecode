#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 将给定数组排序
# @param arr int整型一维数组 待排序的数组
# @return int整型一维数组
#
from typing import List


class Solution:
    def MySort(self, arr: List[int]) -> List[int]:
        # write code here
        self.quick_sort(arr, 0, len(arr) - 1)
        return arr

    def quick_sort(self, arr, low, high):
        # 快排
        mid = self.partition(arr, low, high)
        if mid > low:
            self.quick_sort(arr, low, mid - 1)
        if high > mid:
            self.quick_sort(arr, mid + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        while low < high:
            while arr[low] <= pivot and low < high:
                low += 1

            if arr[low] > pivot:
                arr[high] = arr[low]  # 覆盖空位置
                high -= 1  # 交换完之后，便开始处理另外一边，所以可以直接将另外一边先-1

            while arr[high] >= pivot and low < high:
                high -= 1

            if arr[high] < pivot:
                arr[low] = arr[high]  # 覆盖空位置
                low += 1  # 交换完之后，便开始处理另外一边，所以可以直接将另外一边先+1

            if high == low:
                arr[low] = pivot
        return low


if __name__ == '__main__':
    arr = [3, 1, 6, 9, 0, 4, 1, 4, 6]
    solution = Solution()
    print(solution.MySort(arr))

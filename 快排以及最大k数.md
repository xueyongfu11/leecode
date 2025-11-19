[TOC]



## 快排



## 最大k数

### 基于双指针的方法

```python
class Solution(object):
    def findKthLargest(self, nums, k):
        n = len(nums)
        k = n - k

        def quick_sort(low, high):
            if low == high:
                return nums[low]
            pivot = nums[low]
            left, right = low, high
            left += 1

            while True:
                while left <= right and nums[left] <= pivot:
                    left += 1
                while left <= right and nums[right] >= pivot:
                    right -= 1
                if left >= right:
                    break
                nums[left], nums[right] = nums[right], nums[left]
            # 注意循环结束是break的位置，此时left>=right, right指向左区间的右边界，left指向右区间的左边界，
            # 因此需要将pivot跟right指向的数进行交换
            nums[right], nums[low] = nums[low], nums[right]

            if right == k:
                return nums[k]
            elif right > k:
                return quick_sort(low, right-1)
            else:
                return quick_sort(right+1, high)
        return quick_sort(0, n-1)

```



### 基于单指针的方法

```python
class Solution(object):
    def findKthLargest(self, nums, k):
        n = len(nums)
        k = n - k

        def quick_sort(low, high):
            if low == high:
                return nums[low]
            
            pivot = nums[low]
            index = low  # 循环完之后，index需要指向左区间的右边界,开始时左区间为空，因此指向左区间的前面的位置，即low
            for i in range(low+1, high+1):
                if nums[i] < pivot:
                    index += 1 # 此时index一定指向>=pivot的值
                    nums[index], nums[i] = nums[i], nums[index]
            # 此时index指向左区间的右边界，把pivot的值交换过来
            nums[low], nums[index] = nums[index], nums[low]
            if index == k:
                return nums[k]
            elif index > k:
                return quick_sort(low, index-1)
            else:
                return quick_sort(index+1, high)
        return quick_sort(0, n-1)
```


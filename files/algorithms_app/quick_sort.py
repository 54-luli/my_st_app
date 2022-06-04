import random

code = '''
import random

# 版本1
class Solution:
    def randomPartition(self, arr: [int], low: int, high: int):
        x = random.randint(low, high)
        arr[x], arr[high] = arr[high], arr[x]  # 这里将随机选出的arr[x]与数组末尾的值arr[high]交换了一下，没懂原因
        return self.partition(arr, low, high)

    def partition(self, arr: [int], low: int, high: int):
        x = low - 1  # 最小元素索引
        pivot = arr[high]
        # 所有的数据都只跟pivot比较
        for j in range(low, high):
            # 当前元素小于或等于 pivot
            if arr[j] <= pivot:
                x += 1
                arr[x], arr[j] = arr[j], arr[x]
        # 交换基准值pivot与小于他的最后一个元素arr[x+1]，此时pivot还在末尾，因为前面设置了pivot = arr[high]
        arr[x + 1], arr[high] = arr[high], arr[x + 1]
        return x + 1

    # arr[] --> 排序数组
    # low  --> 起始索引
    # high  --> 结束索引

    # 快速排序函数
    def quickSort(self, arr, low, high):
        if low < high:
            pi = self.randomPartition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)
        return arr

    def sortArray(self, nums):
        return self.quickSort(nums, 0, len(nums) - 1)
'''

compare = '### 平均时间复杂度：O(n*logn)，最好时间复杂度：O(n*logn)，最差时间复杂度：O(n^2)'
compares = '### 空间复杂度：O(logn)，排序方式In-place，数据对象稳定性：不稳定'


def randomPartition(arr: [int], low: int, high: int):
    x = random.randint(low, high)
    arr[x], arr[high] = arr[high], arr[x]  # 这里将随机选出的arr[x]与数组末尾的值arr[high]交换了一下，没懂原因
    return partition(arr, low, high)


def partition(arr: [int], low: int, high: int):
    x = low - 1  # 最小元素索引
    pivot = arr[high]
    # 所有的数据都只跟pivot比较
    for j in range(low, high):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            x += 1
            arr[x], arr[j] = arr[j], arr[x]
    # 交换基准值pivot与小于他的最后一个元素arr[x+1]，此时pivot还在末尾，因为前面设置了pivot = arr[high]
    arr[x + 1], arr[high] = arr[high], arr[x + 1]
    return x + 1


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = randomPartition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    return arr


def sort_array(nums):
    return quickSort(nums, 0, len(nums) - 1)

# if __name__ == '__main__':
#     li = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13]
#     print("排序前的序列为：")
#     for i in li:
#         print(i, end=" ")
#     print("\n排序后的序列为：")
#     # for i in quick_sort(li, 0, len(li) - 1):
#     #     print(i, end=" ")
#     for i in Solution().quickSort(li, 0, len(li) - 1):
#         print(i, end=" ")

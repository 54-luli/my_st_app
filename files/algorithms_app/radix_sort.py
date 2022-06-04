code = '''
class Solution:
    def radixSort(self, arr):
        # 最大位数
        size = len(str(max(arr)))

        # 准备桶
        for i in range(size):
            buckets = [[] for _ in range(10)]
            for num in arr:
                buckets[num // (10 ** i) % 10].append(num)
            arr.clear()
            for bucket in buckets:
                for num in bucket:
                    arr.append(num)

        return arr

    def sortArray(self, nums):
        return self.radixSort(nums)
'''

compare = '### 平均时间复杂度：O(n*k)，最好时间复杂度：O(n*k)，最差时间复杂度：O(n*k)'
compares = '### 空间复杂度：O(n+k)，排序方式Out-place，数据对象稳定性：稳定'


def radixSort(arr):
    # 最大位数
    size = len(str(max(arr)))

    # 准备桶
    for i in range(size):
        buckets = [[] for _ in range(10)]
        for num in arr:
            buckets[num // (10 ** i) % 10].append(num)
        arr.clear()
        for bucket in buckets:
            for num in bucket:
                arr.append(num)

    return arr


def sort_array(nums):
    return radixSort(nums)

# if __name__ == '__main__':
#     lst = [12, 11, 13, 5, 6, 7]
#     print(Solution().sortArray(lst))

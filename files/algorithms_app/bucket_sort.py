code = '''
class Solution:
    # 插入排序
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i
            while j > 0 and arr[j - 1] > temp:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = temp
        return arr

    def bucketSort(self, arr, bucket_size=5):   # 桶的大小
        arr_min, arr_max = min(arr), max(arr)
        bucket_count = (arr_max - arr_min) // bucket_size + 1   # 桶的个数
        buckets = [[] for _ in range(bucket_count)]

        for num in arr:
            buckets[(num - arr_min) // bucket_size].append(num)

        res = []
        for bucket in buckets:
            # self.insertionSort(bucket)
            # res.extend(bucket)
            res.extend(self.insertionSort(bucket))

        return res

    def sortArray(self, nums):
        return self.bucketSort(nums)
'''

compare = '### 平均时间复杂度：O(n+k)，最好时间复杂度：O(n+k)，最差时间复杂度：O(n^2)'
compares = '### 空间复杂度：O(n+k)，排序方式Out-place，数据对象稳定性：稳定'


# 插入排序
def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j - 1] > temp:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp
    return arr


def bucketSort(arr, bucket_size=5):  # 桶的大小
    arr_min, arr_max = min(arr), max(arr)
    bucket_count = (arr_max - arr_min) // bucket_size + 1  # 桶的个数
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        buckets[(num - arr_min) // bucket_size].append(num)

    res = []
    for bucket in buckets:
        # insertionSort(bucket)
        # res.extend(bucket)
        res.extend(insertionSort(bucket))

    return res


def sort_array(nums):
    return bucketSort(nums)

# if __name__ == '__main__':
#     li = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13]
#     print("排序前的序列为：")
#     for i in li:
#         print(i, end=" ")
#     print("\n排序后的序列为：")
#     for i in Solution().sortArray(li):
#         print(i, end=" ")

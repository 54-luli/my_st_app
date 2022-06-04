code = '''
class Solution:
    def merge(self, left_arr, right_arr):
        res = []
        l, r = 0, 0
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] <= right_arr[r]:
                res.append(left_arr[l])
                l += 1
            else:
                res.append(right_arr[r])
                r += 1
        res += left_arr[l:]
        res += right_arr[r:]
        return res

    def mergeSort(self, arr):
        size = len(arr)
        if size < 2:
            return arr
        mid = len(arr) // 2
        # left_arr, right_arr = arr[0: mid], arr[mid:]
        # return self.merge(self.mergeSort(left_arr), self.mergeSort(right_arr))
        return self.merge(self.mergeSort(arr[0: mid]), self.mergeSort(arr[mid:]))

    def sortArray(self, nums):
        return self.mergeSort(nums)
'''

compare = '### 平均时间复杂度：O(n*logn)，最好时间复杂度：O(n*logn)，最差时间复杂度：O(n*logn)'
compares = '### 空间复杂度：O(n)，排序方式Out-place，数据对象稳定性：稳定'


# 2.2归并排序：拆分到单个元素，然后两个两个往上进行递归合并。设置left 和right两个游标,进行合并。
# 时间复杂度：o(nlogn)
def merge(left_arr, right_arr):
    res = []
    l, r = 0, 0
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] <= right_arr[r]:
            res.append(left_arr[l])
            l += 1
        else:
            res.append(right_arr[r])
            r += 1
    res += left_arr[l:]
    res += right_arr[r:]
    return res


def mergeSort(arr):
    size = len(arr)
    if size < 2:
        return arr
    mid = len(arr) // 2
    return merge(mergeSort(arr[0: mid]), mergeSort(arr[mid:]))


def sort_array(nums):
    return mergeSort(nums)

# if __name__ == '__main__':
# li = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13]
# print("排序前的序列为：")
# for i in li:
#     print(i, end=" ")
# print("\n排序后的序列为：")
# for i in merge_sort(li):
#     print(i, end=" ")

# 插入排序：不断地从后面选一个数，然后插入到前面已经有序的序列里。时间复杂度：o(n^2)

code = '''
def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        while i > 0:
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1
            else:
                break
    return arr
'''

compare = '### 平均时间复杂度：O(n^2)，最好时间复杂度：O(n)，最差时间复杂度：O(n^2)'
compares = '### 空间复杂度：O(1)，排序方式In-place，数据对象稳定性：稳定'


def sort_array(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0:
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
            else:
                break
    return arr

# if __name__ == "__main__":
#     lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]
#     print("排序前的序列为：")
#     for i in lists:
#         print(i, end=" ")
#     print("\n排序后的序列为：")
#     for i in insert_sort(lists):
#         print(i, end=" ")

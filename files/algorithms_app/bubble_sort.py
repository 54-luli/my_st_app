code = '''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        count = 0
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
        if 0 == count:
            break
    return arr
'''

compare = '### 平均时间复杂度：O(n^2)，最好时间复杂度O(n），最差时间复杂度：O(n^2)'
compares = '### 空间复杂度：O(1)，排序方式In-place，数据对象稳定性：稳定'


# 冒泡排序：每一趟选出一个最大值，排在最后一个。时间复杂度：o(n^2)

def sort_array(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        count = 0
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
        if 0 == count:
            break
    return arr

# if __name__ == "__main__":
#     lists = [1, 2, 3, 44, 5, 6, 7, 88, 9, 10, 11]
#     print("排序前的序列为：")
#     for i in lists:
#         print(i, end=" ")
#     print("\n排序后的序列为：")
#     for i in bubble_sort(lists):
#         print(i, end=" ")

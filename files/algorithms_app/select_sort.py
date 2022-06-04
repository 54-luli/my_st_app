# 选择排序：每一趟选出一个最小值，放到前面，时间复杂度：o(n^2)

code = '''
def select_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i   # 记录未排序序列中最小数的索引
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # 如果找到最小数，将 i 位置上元素与最小数位置上元素进行交换
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
'''

compare = '### 平均时间复杂度：O(n^2)，最好时间复杂度：O(n^2)，最差时间复杂度：O(n^2)'
compares = '### 空间复杂度：O(1)，排序方式In-place，数据对象稳定性：数组不稳定，链表稳定'


def sort_array(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i  # 记录未排序序列中最小数的索引
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # 如果找到最小数，将 i 位置上元素与最小数位置上元素进行交换
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# if __name__ == "__main__":
#     lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]
#     print("排序前的序列为：")
#     for i in lists:
#         print(i, end=" ")
#     print("\n排序后的序列为：")
#     for i in select_sort(lists):
#         print(i, end=" ")

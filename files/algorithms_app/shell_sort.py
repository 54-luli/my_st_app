# 希尔排序：是一种分组插入排序算法。时间复杂度：o(nlogn) ~ o(n^2)

code = '''
def shell_sort(arr):
    n = len(arr)
    # 分组
    gap = n // 2
    while gap > 0:
        # 进行插排
        for i in range(gap, n):
            j = i
            while j >= gap:
                if arr[j] < arr[j - gap]:
                    arr[j], arr[j - gap] = arr[j - gap], arr[j]
                    j -= gap
                else:
                    break
        gap //= 2
    return arr
'''

compare = '### 平均时间复杂度：O(n*logn)，最好时间复杂度：O(n*(logn)^2)，最差时间复杂度：O(n*(logn)^2)'
compares = '### 空间复杂度：O(1)，排序方式In-place，数据对象稳定性：不稳定'


def sort_array(arr):
    n = len(arr)
    # 分组
    gap = n // 2
    while gap > 0:
        # 进行插排
        for i in range(gap, n):
            j = i
            while j >= gap:
                if arr[j] < arr[j - gap]:
                    arr[j], arr[j - gap] = arr[j - gap], arr[j]
                    j -= gap
                else:
                    break
        gap //= 2
    return arr

    # size = len(arr)
    # gap = size // 2
    # 
    # while gap > 0:
    #     for i in range(gap, size):
    #         temp = arr[i]
    #         j = i
    #         while j >= gap and arr[j - gap] > temp:
    #             arr[j] = arr[j - gap]
    #             j -= gap
    #         arr[j] = temp
    #     gap = gap // 2
    # return arr

# if __name__ == "__main__":
#     lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]
#     print("排序前的序列为：")
#     for i in lists:
#         print(i, end=" ")
#     print("\n排序后的序列为：")
#     for i in shell_sort(lists):
#         print(i, end=" ")

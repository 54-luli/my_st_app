code = '''
# 假设只有根节点需要调整，两棵子树都是堆
def heapify(arr, index, end):
    largest = index
    l = 2 * index + 1  # left = 2*i + 1
    r = 2 * index + 2  # right = 2*i + 2
    if l < end and arr[index] < arr[l]:
        largest = l
    if r < end and arr[largest] < arr[r]:
        largest = r
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]  # 交换
        heapify(arr, largest, end)


def sort_array(arr):
    # 1、建堆
    # 先找到最后一个不是叶子节点的根节点，为(n-2)//2 (若叶子节点为i，则他的父节点为(i-1)//2 )
    # 再向上循环根节点，从小到大
    n = len(arr)
    # 建大顶堆
    # (size-2) // 2 是最后一个非叶节点，叶节点不用调整
    for i in range((n - 2) // 2, -1, -1):
        heapify(arr, i, n)  # 这里可以n-1，区别在于堆调整时只有一个子节点的根节点能不能和子节点的值进行比较，但是实际看有没有问题好像
    # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        # 堆调整算法
        heapify(arr, 0, i)  # 这里可以i-1,但是是上面范围要改为（n-1,-1），可以与思路1和2对比发现差异
    return arr
'''

compare = '### 平均时间复杂度：O(n*logn)，最好时间复杂度：O(n*logn)，最差时间复杂度：O(n*logn)'
compares = '### 空间复杂度：O(1)，排序方式In-place，数据对象稳定性：不稳定'


# 2.3堆排序：构造堆：从小堆到大堆，先看最后一个非叶子节点，从下往上。时间复杂度 ： o(nlogn)
# 向下调整函数的实现, 此处建立大根堆，可实现数组升序排列

# 假设只有根节点需要调整，两棵子树都是堆
def heapify(arr, index, end):
    largest = index
    l = 2 * index + 1  # left = 2*i + 1
    r = 2 * index + 2  # right = 2*i + 2
    if l < end and arr[index] < arr[l]:
        largest = l
    if r < end and arr[largest] < arr[r]:
        largest = r
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]  # 交换
        heapify(arr, largest, end)


def sort_array(arr):
    # 1、建堆
    # 先找到最后一个不是叶子节点的根节点，为(n-2)//2 (若叶子节点为i，则他的父节点为(i-1)//2 )
    # 再向上循环根节点，从小到大
    n = len(arr)
    # 建大顶堆
    # (size-2) // 2 是最后一个非叶节点，叶节点不用调整
    for i in range((n - 2) // 2, -1, -1):
        heapify(arr, i, n)  # 这里可以n-1，区别在于堆调整时只有一个子节点的根节点能不能和子节点的值进行比较，但是实际看有没有问题好像
    # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        # 堆调整算法
        heapify(arr, 0, i)  # 这里可以i-1,但是是上面范围要改为（n-1,-1），可以与思路1和2对比发现差异
    return arr

# if __name__ == '__main__':
#     li = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13]
#     print("排序前的序列为：")
#     for i in li:
#         print(i, end=" ")
#     print("\n排序后的序列为：")
#     for i in heap_sort(li):
#         print(i, end=" ")

import random
import time

random_list1 = [random.randint(1, 1000) for _ in range(5000)]
random_list2 = [random.randint(1, 1000) for _ in range(5000)]

# 插入排序
def insertionsort(arr):
    for i in range(len(arr)):
        preindex = i - 1
        current = arr[i]
        while preindex >= 0 and arr[preindex] > current:
            arr[preindex + 1] = arr[preindex]
            preindex -= 1
        arr[preindex+1] = current
    return arr

#归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 分割数组为两半
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 递归排序两半
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # 合并已排序的两半
    sorted_arr = merge(left_half, right_half)

    return sorted_arr

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # 将剩余的元素添加到合并列表中
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged

start_time1 = time.time()
result1 = insertionsort(random_list1)
end_time1 = time.time()
print(end_time1-start_time1)

start_time2 = time.time()
result2 = merge_sort(random_list2)
end_time2 = time.time()
print(end_time2-start_time2)
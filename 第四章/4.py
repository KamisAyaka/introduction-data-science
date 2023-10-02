def shell_sort(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap,n):
            j = i
            while j > 0:
                if array[j-gap] > array[j]:
                    array[j-gap] , array[j] = array[j],array[j-gap]
                    j -= gap
                else:
                    break
        gap //= 2
    return array

a = input().split(",")
shell_sort(a)
print(a)
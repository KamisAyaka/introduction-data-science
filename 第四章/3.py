def insertionSort(arr):
    for i in range(len(arr)):
        preindex = i - 1
        current = arr[i]
        while preindex >= 0 and arr[preindex]>current:
            arr[preindex+1] = arr[preindex]
            preindex -= 1
        arr[preindex+1] =current

a = input().split(",")
insertionSort(a)
print(a)
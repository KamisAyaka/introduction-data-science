import random
import time

random_list1 = [random.randint(1, 10000) for _ in range(1000)]
def select_sort(array):
    for i in range(len(array)):
        x = i
        for j in range(i , len(array)):
            if array[j]<array[x]:
                x = j
        array[i], array[x] = array[x],array[i]
    return array

start_time1 = time.time()
result1 = select_sort(random_list1)
end_time1 = time.time()
print(end_time1-start_time1)

import math


def bucketSort(arrr):
    buckets = round(math.sqrt(len(arrr)))
    max_value = max(arrr)
    temp_arr = []

    for i in range(buckets):
        temp_arr.append([])

    for j in arrr:
        b_index = math.ceil(j * buckets / max_value)
        temp_arr[b_index - 1].append(j)

    for i in range(buckets):
        temp_arr[i].sort()  # Use best sort algorithm here

    k = 0
    for i in range(buckets):
        for j in range(len(temp_arr[i])):
            arrr[k] = temp_arr[i][j]
            k += 1


arr = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]
print("Before Sorting : ", arr)
bucketSort(arr)
print("After Sorting : ", arr)

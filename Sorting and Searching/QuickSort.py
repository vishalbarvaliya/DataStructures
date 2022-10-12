def partition(arr, start, end):
    pivot = arr[end]
    p_index = start

    for j in range(start, end):
        if arr[j] <= pivot:
            arr[p_index], arr[j] = arr[j], arr[p_index]
            p_index += 1

    arr[p_index], arr[end] = arr[end], arr[p_index]

    return p_index


def quickSort(arr):
    quickSortUtil(arr, 0, len(arr) - 1)


def quickSortUtil(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quickSortUtil(arr, start, pivot - 1)
        quickSortUtil(arr, pivot + 1, end)


# arr = [12, 11, 13, 5, 6, 7]
arr = [5, 15, 6, 87, 54, 9, 98, 52, 3]
print("Before : ", arr)
quickSort(arr)
print("After : ", arr)

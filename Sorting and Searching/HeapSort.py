

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # Left child
    r = 2 * i + 2  # Right child

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    size = len(arr)
    # Building Max heap
    for i in range(size // 2 - 1, -1, -1):
        heapify(arr, size, i)

    # One by one extract element and put at end
    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # Swap first and last
        heapify(arr, i, 0)


arr = [50, 6, 25, 69, 22, 45, 5, 1, 7]
print("Before Sorting : ", arr)
heapSort(arr)
print("After Sorting : ", arr)

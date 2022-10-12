

def countSort(arr, exp1):
    size = len(arr)
    count = [0 for _ in range(10)]
    output = [0 for _ in range(size)]

    for i in range(size):
        index = arr[i] / exp1
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(size - 1, -1, -1):
        index = arr[i] / exp1
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1

    for i in range(size):
        arr[i] = output[i]


def radixSort(arr):
    max_value = max(arr)
    exp = 1
    # Passes = digits of maximum value
    while max_value/exp > 0:
        countSort(arr, exp)
        exp *= 10


arr = [50, 6, 250, 690, 212, 45, 5, 1, 7]
print("Before Sorting : ", arr)
radixSort(arr)
print("After Sorting : ", arr)
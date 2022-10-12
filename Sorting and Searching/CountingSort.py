

def countSort(arr):
    max_value = max(arr)
    count = [0 for _ in range(max_value + 1)]  # To store count of individual element
    output = [0 for _ in range(len(arr))]  # This will have sorted array

    # Storing the count of each element
    for i in range(len(arr)):
        count[arr[i]] += 1

    # Change count[i] so that it contains actual positions of this element in output array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    # Overriding main array
    for i in range(len(output)):
        arr[i] = output[i]


arr = [50, 6, 25, 69, 22, 45, 5, 1, 7]
print("Before Sorting : ", arr)
countSort(arr)
print("After Sorting : ", arr)



def insertionSort(arrr):
    length = len(arrr)
    for i in range(1, length):
        key = arrr[i]
        j = i - 1
        while j >= 0 and key < arrr[j]:
            arrr[j + 1] = arrr[j]
            j -= 1
        arrr[j + 1] = key


arr = [50, 6, 25, 69, 22, 45, 5, 1, 7]
print("Before Sorting : ", arr)
insertionSort(arr)
print("After Sorting : ", arr)



def selectionSort(arrr):
    length = len(arrr)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arrr[j] < arrr[min_index]:
                min_index = j
        arrr[min_index], arrr[i] = arrr[i], arrr[min_index]


arr = [50, 6, 25, 69, 22, 45, 5, 1, 7]
print("Before Sorting : ", arr)
selectionSort(arr)
print("After Sorting : ", arr)

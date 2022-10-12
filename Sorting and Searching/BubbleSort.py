from random import randint


def bubbleSort(arrr):
    length = len(arrr)
    swapped = False
    for i in range(length - 1):
        # range(length) also works but last i elements are already in place.
        for j in range(length - i - 1):
            if arrr[j] > arrr[j + 1]:
                swapped = True
                arrr[j], arrr[j + 1] = arrr[j + 1], arrr[j]

        # if we haven't made a single swap, we can exit the main loop.
        if not swapped:
            return


arr = [50, 6, 25, 69, 22, 45, 5, 1, 7]
print("Before Sorting : ", arr)
bubbleSort(arr)
print("After Sorting : ", arr)

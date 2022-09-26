def findMaxRec(arr, n):
    assert n >= 1, 'The array must contain atleast 1 element.'
    if n == 1:
        return arr[0]
    return max(arr[n - 1], findMaxRec(arr, n - 1))

arr = [5,10,2,7,9]
print(findMaxRec(arr, len(arr)))

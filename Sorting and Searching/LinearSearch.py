

def search(arr, data):
    if arr:
        for i in range(len(arr)):
            if arr[i] == data:
                return i
    return -1


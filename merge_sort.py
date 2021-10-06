def merge(arr, left, right):
    compares = 0
    i, j, k = 0, 0, 0
    compares += 2
    while i < len(left) and j < len(right):
        compares += 2
        
        compares += 1
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1

    compares += 1
    while i < len(left):
        compares += 1
        arr[k] = left[i]
        i += 1
        k += 1

    compares += 1
    while j < len(right):
        compares += 1
        arr[k] = right[j]
        j += 1
        k += 1

    return compares


def merge_sort(arr):
    compares = 0
    if len(arr) > 1:
        q = len(arr) // 2
        left = arr[:q]
        right = arr[q:]
        merge_sort(left)
        merge_sort(right)
        compares += merge(arr, left, right)
    return compares

# arr = [3, 1, 0, 2]
# merge_sort(arr)
# print(arr)
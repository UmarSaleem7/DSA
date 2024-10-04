def partition(arr, low, high):
    pivot_value = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] < pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)
        return arr


data = [8, 7, 2, 1, 0, 9, 6]
n = len(data)
print(quicksort(data, 0, n-1))

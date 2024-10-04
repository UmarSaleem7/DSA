def merge_sorting(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2

        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sorting(left_arr)
        merge_sorting(right_arr)

        return merge(arr, left_arr, right_arr)


def merge(arr, arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i = j = k = 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1

    return arr


def main():
    arr = [4, 2, 8, 3, 98, 45, 22, 56, 1]
    print(merge_sorting(arr))


main()

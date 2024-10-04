def insertion_sorting(arr):
    for i in range(1, len(arr)):
        element = arr[i]
        j = i-1
        while j >= 0 and element < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = element
    return arr


def main():
    arr = [0, 10, 8, 6, 2, 3, 1]
    print(insertion_sorting(arr))


main()

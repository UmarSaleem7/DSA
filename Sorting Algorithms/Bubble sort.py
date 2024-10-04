def bubble_sorting(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():
    x = [8, 0, 7, 1, 3]
    print(bubble_sorting(x))


main()

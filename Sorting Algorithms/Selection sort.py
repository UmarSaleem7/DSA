def selection_sorting(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list


def main():
    x = [8, 0, 7, 1, 3]
    print(selection_sorting(x))


main()

def counting(arr):
    max_element = max(arr)
    count = [0] * (max_element+1)
    for i in range(len(arr)):
        count[arr[i]] += 1
    return count


def cumulativesum(count):
    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]
    return count


def countingsort(arr):
    output = [0] * len(arr)
    count = counting(arr)
    count = cumulativesum(count)
    for num in arr:
        count[num] = count[num] - 1
        output[count[num]] = num
    return output


def main():
    arr = [2, 1, 1, 2, 2, 2, 3, 3, 5, 4, 6, 3]
    print(countingsort(arr))


main()

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    sortedLeft = mergeSort(left)
    sortedRight = mergeSort(right)

    return merge(sortedLeft, sortedRight)


if __name__ == "__main__":
    arr = [5, 67, 9, 0, 5, 9, 73, 46, 7, 97, 614, 907, 97, 5]
    print(f"Unsorted arr {arr}")

    sorted = mergeSort(arr)
    print(f"Sorted arr : {sorted}")

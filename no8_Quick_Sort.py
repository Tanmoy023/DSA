def partitioning(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low=0, high=None):
    if high == None:
        high = len(arr) - 1
    if low < high:
        partition_index = partitioning(arr, low, high)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)


if __name__ == "__main__":
    arr = [5, 67, 9, 0, 5, 9, 73, 46, 7, 97, 614, 907, 97, 5]
    print(f"Unsorted arr {arr}")

    quick_sort(arr)
    print(f"Sorted arr : {arr}")

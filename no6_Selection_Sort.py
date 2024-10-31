def Selection_Sort(arr):
    n = len(arr)
    for i in range(n - 1):
        minIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        minVal = arr.pop(minIndex)
        arr.insert(i, minVal)


if __name__ == "__main__":
    arr = [5, 67, 9, 0, 5, 9, 73, 46, 7, 97, 614, 907, 97, 5]
    print(f"Unsorted arr {arr}")

    Selection_Sort(arr)
    print(f"Sorted arr : {arr}")

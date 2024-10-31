def Insertion_Sort(arr):
    n = len(arr)
    for i in range(1, n):
        insert_index = i
        currentVal = arr.pop(i)
        for j in range(i - 1, -1, -1):
            if arr[j] > currentVal:
                insert_index = j
        arr.insert(insert_index, currentVal)


if __name__ == "__main__":
    arr = [5, 67, 9, 0, 5, 9, 73, 46, 7, 97, 614, 907, 97, 5]
    print(f"Unsorted arr {arr}")

    Insertion_Sort(arr)
    print(f"Sorted arr : {arr}")

def Count_sort(arr):
    arr_max = max(arr)
    count = [0] * (arr_max + 1)
    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1
    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1


if __name__ == "__main__":
    arr = [5, 67, 9, 0, 5, 9, 73, 46, 7, 97, 614, 907, 97, 5]
    print(f"Unsorted arr {arr}")

    Count_sort(arr)
    print(f"Sorted arr : {arr}")

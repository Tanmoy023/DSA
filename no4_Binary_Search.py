def Binary_Search(arr, val):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if val == arr[mid]:
            print(f"{val} is present in index-{mid}")
            return
        elif val < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print(f"{val} is not present in given Array!")


def Binary_Search_Recurtion(arr, val, low, high):
    if low > high:
        return
    mid = (low + high) // 2
    if mid >= len(arr) or mid < 0:
        print(f"{val} is not present in given Array!")
        return

    if val == arr[mid]:
        print(f"{val} is present in index-{mid}")
    elif val < arr[mid]:
        Binary_Search_Recurtion(arr, val, low, mid - 1)
    else:
        Binary_Search_Recurtion(arr, val, mid + 1, high)


if __name__ == "__main__":
    arr = [12, 15, 19, 21, 28, 33, 54, 65, 70, 88, 95, 100]
    # Binary_Search(arr,88)
    Binary_Search_Recurtion(arr, 33, 0, len(arr))
    Binary_Search_Recurtion(arr, 110, 0, len(arr))

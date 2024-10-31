def Linear_Search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            print(f"{val} is present in index-{i}")
            return
    print(f"{val} is not present in given array!")


if __name__ == "__main__":
    arr = [12, 15, 19, 21, 28, 33, 54, 65, 70, 88, 95, 100]
    Linear_Search(arr, 88)
    Linear_Search(arr, 110)

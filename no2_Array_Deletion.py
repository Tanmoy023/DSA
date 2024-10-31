class Array:
    def __init__(self):
        self.arr = [5, 7, 12, 26, 38, 50, 65, 78, 81, 98, 100]

    def delete_values(self, values):
        for i in range(len(values)):
            try:
                self.arr.remove(values[i])
            except:
                print(f"Given value {values[i]} is not in Array!")

    def delete_at_end(self):
        self.arr.remove(self.arr[len(self.arr)-1])

    def delete_at_first(self):
        self.arr.remove(self.arr[0])

    def delete_at_index(self, index):
        if index < 0 or index > len(self.arr):
            print(f"invalid index!")
            return
        if index == len(self.arr):
            self.delete_at_end()
        elif index == 0:
            self.delete_at_first()
        else:
            self.arr.remove(self.arr[index])


if __name__ == "__main__":
    a = Array()
    a.delete_values([50, 65, 10])
    a.delete_at_first()
    a.delete_at_end()
    a.delete_at_index(0)
    print(a.arr)

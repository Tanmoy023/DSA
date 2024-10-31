class Array:
    def __init__(self):
        self.arr = []

    def insert_values(self, values):
        for i in range(len(values)):
            self.arr.append(values[i])

    def insert_at_end(self, val):
        self.arr.append(val)

    def insert_at_first(self, val):
        self.arr.insert(0, val)

    def insert_at_index(self, index, val):
        if index < 0 or index > len(self.arr):
            print(f"invalid index!")
            return
        if index == len(self.arr):
            self.insert_at_end(val)
        elif index == 0:
            self.insert_at_first(val)
        else:
            self.arr.insert(index, val)


if __name__ == "__main__":
    a = Array()
    values = [5, 7, 12, 26, 38]
    a.insert_values(values)
    a.insert_at_first(0)
    a.insert_at_end(100)
    a.insert_at_index(3, 1000)
    print(a.arr)

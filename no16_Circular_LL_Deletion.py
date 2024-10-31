class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = node()
        self.head.next = self.head

    def is_Empty(self):
        if self.head.data == None:
            return True
        return False

    def display(self):
        if self.head.data == None:
            print("-_- LinkedList is empty!")
            return
        itr = self.head
        list = str(itr.data) + "-->"
        itr = itr.next
        while itr != self.head:
            list += str(itr.data) + "-->"
            itr = itr.next
        list += "Head"
        print(list)

    def get_length(self):
        ptr = self.head
        count = 0
        if self.head.data == None:
            return -1
        while ptr.next != self.head:
            ptr = ptr.next
            count += 1
        # print(f"The length of this Circular LinkedList is : {count}")
        return count

    def Insertion(self, list):
        self.head = node(list[0])
        ptr = self.head
        for i in range(1, len(list)):
            n = node(list[i])
            ptr.next = n
            ptr = ptr.next
        ptr.next = self.head

    def Delete_First(self):
        ptr = self.head
        while ptr.next != self.head:
            ptr = ptr.next
        # print(f"<<{ptr.data}>>")
        n = self.head.next
        ptr.next = n
        self.head = n

    def Delete_End(self):
        ptr = self.head.next
        while ptr.next != self.head:
            prevPtr = ptr
            ptr = ptr.next
        prevPtr.next = self.head

    def Delete_at_value(self, value):
        if self.head.data == value:
            self.Delete_First()
            return
        prevPtr = self.head
        ptr = prevPtr.next
        while ptr.data != value and ptr != self.head:
            prevPtr = ptr
            ptr = ptr.next
        if ptr.data == value:
            prevPtr.next = ptr.next
        else:
            print(f"given value({value}) is not found in this Circular LinkedList")

    def Delete_Values(self, list):
        for i in range(len(list)):
            self.Delete_at_value(list[i])

    def Delete_At_index(self, index):
        if index == 0:
            self.Delete_First()
            return
        if index == self.get_length():
            self.Delete_End()
            return
        ptr = self.head
        for i in range(index):
            ptr = ptr.next
        self.Delete_at_value(ptr.data)


if __name__ == "__main__":
    ll = LinkedList()
    ll.Insertion([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # ll.Delete_First()
    # ll.Delete_End()
    # ll.Delete_at_value(5)
    # ll.Delete_Values([1, 5, 66, 9, 10])
    ll.Delete_At_index(5)

    ll.display()
    print(f"The length of this Circular LinkedList is : {ll.get_length()}")

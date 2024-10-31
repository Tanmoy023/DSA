class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head == None:
            print("Linked list is empty!")
            return
        ptr = self.head
        list = ""
        while ptr != None:
            list += str(ptr.data) + "-->"
            ptr = ptr.next
        list += "None"
        print(list)

    def get_length(self):
        ptr = self.head
        count = 0
        while ptr != None:
            ptr = ptr.next
            count += 1
        # print(f"Length of this Linked List is : {count}")
        return count

    def Insertion(self, list):
        ptr = node(list[0])
        self.head = ptr
        for i in range(1, len(list)):
            new = node(list[i])
            ptr.next = new
            ptr = new

    def Delete_At_Start(self):
        self.head = self.head.next

    def Delete_At_Last(self):
        ptr = self.head
        while ptr.next.next != None:
            ptr = ptr.next
        ptr.next = None

    def Delete_Value(self, val):
        if self.head.data == val:
            self.Delete_At_Start()
            return

        ptr = self.head
        while ptr.next != None and ptr.next.data != val:
            ptr = ptr.next
        if ptr.next != None and ptr.next.data == val:
            ptr.next = ptr.next.next
            return
        print(f"Given value {val} is not present in LinkedList")

    def Delete_Values(self, list):
        for i in range(len(list)):
            self.Delete_Value(list[i])

    def Delete_At_Index(self, index):
        if index < 0 or index > self.get_length() - 1:
            print("Invalid Index!")
            return

        ptr = self.head
        count = 0
        for i in range(index):
            ptr = ptr.next
            count += 1
        # print(f"<<{ptr.data}>>")
        self.Delete_Value(ptr.data)


if __name__ == "__main__":
    ll = LinkedList()
    ll.Insertion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # ll.Delete_At_Start()
    # ll.Delete_At_Last()
    # ll.Delete_At_Index(9)
    # ll.Delete_Value(6)
    ll.Delete_Values([3, 7, 10])

    ll.display()
    print(f"Length of this Linked List is : {ll.get_length()}")

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

    def Insert_At_First(self, data):
        self.head = node(data, self.head)

    def Insert_At_Last(self, data):
        if self.head == None:
            self.Insert_At_First(data)
        else:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = node(data)

    def Insert_values(self, list):
        for i in range(len(list)):
            self.Insert_At_Last(list[i])

    def Insert_At_Index(self, index, data):
        if index < 0 or index > self.get_length():
            print("Invalid Index!")
            return

        if index == 0:
            self.Insert_At_First(data)
            return

        ptr = self.head
        for i in range(index - 1):
            ptr = ptr.next

        ptrNext = ptr.next
        new = node(data)
        ptr.next = new
        new.next = ptrNext

    def Insert_At_Value(self, value, data):
        ptr = self.head

        index = 0
        while ptr.data != value and ptr != None:
            ptr = ptr.next
            index += 1

        if ptr.data == value:
            self.Insert_At_Index(index, data)
            return

        print(f"Given value {value} is not present in this Linked List")


if __name__ == "__main__":
    ll = LinkedList()

    ll.Insert_At_First(1)
    ll.Insert_At_Last(2)
    ll.Insert_values([3, 4, 5])
    ll.Insert_At_Index(5, 10)
    ll.Insert_At_Value(5, 100)

    ll.display()
    print(f"Length of this Linked List is : {ll.get_length()}")

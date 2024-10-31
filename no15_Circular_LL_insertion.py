class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = node()
        self.head.next = self.head

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

    def Insert_At_First(self, data):
        n = node(data)
        if self.head.data == None:
            self.head = n
            self.head.next = self.head
            return
        ptr = self.head
        while ptr.next != self.head:
            ptr = ptr.next
        ptr.next = n
        n.next = self.head
        self.head = n

    def Insert_At_Last(self, data):
        n = node(data)
        if self.head.data == None:
            self.Insert_At_First(data)
            return
        ptr = self.head
        while ptr.next != self.head:
            ptr = ptr.next
        ptrNext = ptr.next
        ptr.next = n
        n.next = ptrNext

    def Insert_Values(self, list):
        for i in range(len(list)):
            self.Insert_At_Last(list[i])

    def Insert_At_Index(self, index, data):
        if index < 0 or index > self.get_length():
            print("-_- Invalid Index!")
            return
        if index == 0:
            self.Insert_At_First(data)
            return
        if index == self.get_length() + 1:
            self.Insert_At_Last(data)
            return
        ptr = self.head
        for i in range(index - 1):
            ptr = ptr.next
        ptrNext = ptr.next
        n = node(data)
        ptr.next = n
        n.next = ptrNext

    def Insert_At_Value(self, val, data):
        ptr = self.head
        index = 0
        while ptr.next != self.head and ptr.data != val:
            ptr = ptr.next
            index += 1
        # print(f"<<{index}>>")
        if ptr.data == val:
            self.Insert_At_Index(index, data)
            return
        print(f"-_- Given value {val} is not present in this Circular LinkedList!")


if __name__ == "__main__":
    ll = LinkedList()

    ll.Insert_At_First(0)
    ll.Insert_At_Last(1)
    ll.Insert_Values([2, 5, 6])
    ll.Insert_At_Index(3, 3)
    ll.Insert_At_Value(5, 4)

    ll.display()
    print(f"The length of this Circular LinkedList is : {ll.get_length()}")

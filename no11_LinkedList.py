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
        itr = self.head
        list = ""
        while itr != None:
            list += str(itr.data) + "-->"
            itr = itr.next
        list += "None"
        print(list)


if __name__ == "__main__":
    ll = LinkedList()

    n = node(1, None)
    ll.head = n

    second = node(2, None)
    n.next = second

    third = node(3, None)
    second.next = third

    forth = node(4, None)
    third.next = forth

    fifth = node(5, None)
    forth.next = fifth

    ll.display()

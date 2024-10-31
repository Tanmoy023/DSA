class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Double_LinkedList:
    def __init__(self):
        self.head = Node(None)

    def insertion(self, list):
        new_node = Node(list[0])
        self.head = new_node
        last = self.head
        for e in list[1:]:
            new_node = Node(e)
            last.next = new_node
            new_node.prev = last
            last = last.next

    def get_length(self):
        ptr = self.head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        return count

    def is_Empty(self):
        if not self.head:
            return True
        return False

    def display_forword(self):
        if self.is_Empty():
            print("Empty Double linkedList !")
        dl = ""
        ptr = self.head
        while ptr:
            dl += str(ptr.data) + "-->"
            ptr = ptr.next
        dl += "None(next)"
        print(dl)

    def display_backword(self):
        if self.is_Empty():
            print("Empty Double linkedList !")

        ptr = self.head
        while ptr.next:
            ptr = ptr.next

        dl = ""
        while ptr:
            dl += str(ptr.data) + "-->"
            ptr = ptr.prev
        dl += "None(prev)"
        print(dl)


if __name__ == "__main__":
    dl = Double_LinkedList()
    dl.insertion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    dl.display_forword()
    dl.display_backword()
    dl.get_length
    print(f"The length of this double linkedList : {dl.get_length()}")

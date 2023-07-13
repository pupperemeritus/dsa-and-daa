class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class L_L:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Empty")
        else:
            i = self.head
            while i is not None:
                print(i.data)
                i = i.next

    def add_start(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head = new

    def add_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            i = self.head
            while i.next is not None:
                i = i.next
            i.next = new

    def delete_beginning(self):
        if self.head is None:
            print("list is already empty")
        else:
            t = self.head
            self.head = self.head.next
            t.next = None

    def delete_end(self):
        if self.head is None:
            print("list is already empty")
        elif self.head.next is None:
            self.head = None
        else:
            i = self.head
            while i.next.next is not None:
                i = i.next
            i.next = None

    def add_before(self, data, x):
        new = Node(data)
        if self.head is None:
            print("list is empty")
            return
        if self.head.data == x:
            new.next = self.head
            self.head = new
        else:
            i = self.head
            while i.next is not None:
                if i.next.data == x:
                    new.next = i.next
                    i.next = new
                    break
                i = i.next

    def add_after(self, data, x):
        new = Node(data)
        if self.head is None:
            print("list is empty")
            return
        if self.head.data == x:
            new.next = self.head.next
            self.head.next = new
        else:
            i = self.head
            while i.next.next is not None:
                if i.data == x:
                    new.next = i.next
                    i.next = new
                    break
                i = i.next

    def delete_before(self, x):
        if self.head is None:
            print("List is empty")
        else:
            i = self.head
            while i.next.next is not None:
                if i.next.next.data == x:
                    i.next = i.next.next
                i = i.next

    def delete_after(self, x):
        if self.head is None:
            print("List is empty")
        else:
            i = self.head
            while i.next.next is not None:
                if i.data == x:
                    i.next = i.next.next
                i = i.next

    def isEmpty(self):
        return self.head is None


if __name__ == "__main__":
    a = L_L()
    for i in range(10):
        a.add_end(i*10)
    a.delete_beginning()
    a.delete_end()
    a.delete_after(40)
    a.add_before(62, 40)
    a.add_after(44, 40)
    a.delete_before(70)
    a.print_ll()

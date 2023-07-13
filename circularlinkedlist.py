class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class C_L_L:
    def __init__(self):
        self.head = None
#

    def print_ll(self):
        if self.head is None:
            print("Empty")
        else:
            i = self.head
            while True:
                print(i.data)
                i = i.next
                if i == self.head:
                    break

#
    def add_start(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            new.next = self.head
        elif self.head.next is self.head:
            self.head.next.next = new
            new.next = self.head
            self.head = new
        else:
            i = self.head
            while i.next is not self.head.next:
                i = i.next
            i.next = new
            new.next = self.head
            self.head = new
            new.next = self.head.next

    def add_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            self.head.next = self.head
        else:
            i = self.head
            while i.next is not self.head:
                i = i.next
            i.next = new
            new.next = self.head

#
    def delete_beginning(self):
        if self.head is None:
            print("list is already empty")
        else:
            i = self.head
            while True:
                if i.next is self.head:
                    break
                i = i.next
            i.next = self.head.next
            self.head = self.head.next

#
    def delete_end(self):
        if self.head is None:
            print("list is already empty")
        elif self.head.next is self.head:
            self.head = None
        else:
            i = self.head
            while i.next.next is not self.head:
                i = i.next
            i.next = self.head

    def add_before(self, data, x):
        new = Node(data)
        if self.head is None:
            print("list is empty")
            return
        elif self.head.data == x:
            i = self.head
            while i.next.next is not self.head:
                i = i.next
            i.next = new
            new.next = self.head
            self.head = new
        else:
            i = self.head
            while i.next is not self.head:
                if i.next.data == x:
                    new.next = i.next
                    i.next = new
                    break
                i = i.next

#
    def add_after(self, data, x):
        new = Node(data)
        if self.head is None:
            print("list is empty")
        elif self.head.data == x:
            new.next = self.head.next
            self.head.next = new
        else:
            i = self.head
            while i.next.next is not self.head:
                if i.data == x and i.next is not self.head:
                    new.next = i.next
                    i.next = new
                    break
                elif i.data == x and i.next is self.head:
                    new.next = self.head
                    i.next = new
                    break
                i = i.next

#
    def delete_before(self, x):
        if self.head is None:
            print("List is empty")
        else:
            i = self.head
            while i.next.next is not self.head:
                if i.next.next.data == x and i.next.next.next is not self.head:
                    i.next = i.next.next
                    break
                i = i.next

    def delete_after(self, x):
        if self.head is None:
            print("List is empty")
        else:
            i = self.head
            while i.next.next is not self.head:
                if i.data == x and i.next.next is not self.head:
                    i.next = i.next.next
                    break
                elif i.data == x and i.next.next is self.head:
                    i.next = self.head.next
                    self.head = self.head.next
                    break
                i = i.next


if __name__ == "__main__":
    a = C_L_L()
    for i in range(10):
        a.add_end(i*10)
    a.delete_beginning()
    a.delete_end()
    a.delete_after(40)
    a.add_before(62, 40)
    a.add_after(44, 40)
    a.delete_before(70)
    a.print_ll()

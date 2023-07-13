class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class D_C_L_L:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Empty")
        else:
            i = self.head
            while i is not self.head.prev:
                print(i.data)
                i = i.next
            print(i.data)

    def add_start(self, data):
        new = Node(data)
        if self.head is None:
            self.head.prev = self.head.next = self.head = new
        else:
            new.next = self.head
            new.prev = self.head.prev
            self.head.prev = new
            self.head = new

    def add_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            new.next = new
            new.prev = new
        else:
            i = self.head
            while True:
                i = i.next
                if i is self.head.prev:
                    break
            i.next = new
            new.prev = i
            self.head.prev = new

    def delete_beginning(self):
        if self.head is None:
            print("list is already empty")
        else:
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("list is already empty")
        else:
            i = self.head
            while True:
                i = i.next
                if i is self.head.prev.prev:
                    break
            i.next = self.head
            self.head.prev = i

    def print_rev(self):
        i = self.head.prev
        while True:
            print(i.data)
            i = i.prev
            if i is self.head.prev:
                break

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
            while True:
                if i.next.data == x:
                    i.next.prev = new
                    new.next = i.next
                    i.next = new
                    new.prev = i
                    break
                i = i.next
                if i is self.head:
                    break

    def insertinbtw(self, data):
        n = 1
        i = self.head.next
        while i.next is not self.head:
            i = i.next
            n += 1
        m = 0
        i = self.head
        while m <= n//2:
            i = i.next
            m += 1
        self.add_after(data, i.data)

    def add_after(self, data, x):
        new = Node(data)
        if self.head is None:
            print("list is empty")
        if self.head.data == x:
            new.next = self.head.next
            self.head.next = new
            new.prev = self.head
        else:
            i = self.head
            while True:
                if i.data == x:
                    new.next = i.next
                    i.next.prev = new
                    i.next = new
                    new.prev = i
                    break
                i = i.next
                if i is self.head:
                    break

    def delete_before(self, x):
        if self.head is None:
            print("List is empty")
        else:
            i = self.head
            while True:
                if i.data == x:
                    i.prev = i.prev.prev
                    i.prev.next = i
                    break
                i = i.next
                if i is self.head:
                    break

    def delete_after(self, x):
        if self.head is None:
            print("List is empty")
        else:
            i = self.head
            while i is not None:
                if i.data == x:
                    i.next = i.next.next
                    i.next.prev = i
                    break
                i = i.next
                if i is self.head:
                    break

    def delete_index(self, i):
        j = self.head
        k = 0
        while k < i and j.next is not self.head:
            k += 1
            j = j.next
        if k == i:
            n = self.head
            m = 0
            while m < k:
                n = n.next
                m += 1
            n.prev.next = n.next
            n.next.prev = n.prev
            n.prev = n.next = None


if __name__ == "__main__":
    a = D_C_L_L()
    for i in range(10):
        a.add_end(i*10)
    a.delete_beginning()
    a.delete_end()
    a.delete_after(40)
    a.add_before(62, 40)
    a.add_after(44, 40)
    a.delete_index(1)
    a.delete_before(70)
    a.insertinbtw("btw")
    a.print_ll()
    a.print_rev()

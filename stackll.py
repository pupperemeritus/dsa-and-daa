class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            new = Node(data)
            new.prev = self.top
            self.top = new
            self.size += 1

    def pop(self):
        if self.top is None:
            print("Stack underflow")
        else:
            data = self.top.data
            self.top = self.top.prev
            self.size -= 1
            return data

    def peek(self):
        return self.top.data

    def isEmpty(self):
        return self.size == 0


if __name__ == "__main__":
    s = Stack()
    for i in range(5):
        s.push(i)
    print(s.pop())
    print(s.peek())
    print(s.isEmpty())
    print(s.size)

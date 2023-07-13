from stack import Stack


class Queue:
    def __init__(self):
        self.que1 = Stack()
        self.que2 = Stack()
        self.size = 0

    @staticmethod
    def transfer(st1, st2):
        while not st1.isEmpty():
            st2.push(st1.pop())

    def enqueue(self, data):
        self.que1.push(data)
        self.size += 1

    def dequeue(self):
        self.transfer(self.que1, self.que2)
        recent = self.que2.pop()
        self.size -= 1
        self.transfer(self.que2, self.que1)
        return recent

    def isEmpty(self):
        return self.size == 0

    def queueFront(self):
        self.transfer(self.que1, self.que2)
        front = self.que2.peek()
        self.transfer(self.que2, self.que1)
        return front

    def queueRear(self):
        return self.que1.peek()


if __name__ == "__main__":
    qu = Queue()
    for i in range(10):
        qu.enqueue(i)
    print(qu.queueFront(), qu.queueRear())
    qu.dequeue()
    print(qu.queueFront())
    print(qu.size, qu.isEmpty())

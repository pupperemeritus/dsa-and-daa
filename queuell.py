class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        if self.rear is None:
            self.rear = self.front = Node(data)
        else:
            new = Node(data)
            new.prev = self.rear
            self.rear = new
        self.size += 1

    def dequeue(self):
        if self.front is None:
            print("Queue underflow")
        else:
            i = self.rear
            while i.prev is not self.front:
                i = i.prev
            i.prev = None
            self.front = i
            self.size -= 1

    def isEmpty(self):
        return self.rear is None

    def queueFront(self):
        if self.size > 0:
            return self.front.data
        else:
            return None

    def queueRear(self):
        if self.size > 0:
            return self.rear.data
        else:
            return None


if __name__ == "__main__":
    qu = Queue()
    for i in range(5):
        qu.enqueue(i)
    print(f"Front : {qu.queueFront()}\nRear : {qu.queueRear()}")
    print(qu.isEmpty(), qu.size)
    qu.dequeue()
    print(qu.queueFront())

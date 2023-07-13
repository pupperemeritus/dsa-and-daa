import heapq


class Queuenode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"{self.data}[{self.priority}]"


class PriorityQueue:
    def __init__(self):
        self.qu = []

    def enqueue(self, data, priority):
        self.qu.append(Queuenode(data, priority))
        heapq.heapify(self.qu)

    def dequeue(self):
        try:
            return heapq.heappop(self.qu)
        except IndexError:
            pass

    def __repr__(self):
        return f"{self.qu}"


if __name__ == "__main__":
    pq = PriorityQueue()
    data = [3, 23, 12, 36, 47, 58, 67, 45, 45]
    prio = [1, 2, 3, 3, 3, 2, 1, 1, 2]
    for i in range(len(data)):
        pq.enqueue(data[i], prio[i])
    print(pq)
    pq.dequeue()
    print(pq)

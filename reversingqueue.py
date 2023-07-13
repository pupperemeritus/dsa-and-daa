from queue import Queue
from stack import Stack


def reverse(queue):
    """Reverses the items in a queue."""
    stack = Stack()  # Create an empty stack

    # Move items from the queue to the stack
    while not queue.isEmpty():
        stack.push(queue.dequeue())

    # Move items from the stack back to the queue, reversing their order
    while not stack.isEmpty():
        queue.enqueue(stack.pop())


def reverse_rec(queue):
    """
    Reverses the elements in a queue using recursion.

    Args:
        queue: The queue to be reversed.

    Returns:
        None
    """
    if queue.isEmpty():
        return

    # Remove the first element from the queue
    t = queue.dequeue()

    # Reverse the remaining elements in the queue
    reverse(queue)

    # Enqueue the first element at the end of the queue
    queue.enqueue(t)


if __name__ == "__main__":
    qu = Queue()
    st = input("Enter String : ")
    for i in st:
        qu.enqueue(i)
    print(qu.queueFront(), qu.queueRear())
    reverse(qu)
    print(qu.queueFront(), qu.queueRear())
    reverse_rec(qu)
    print(qu.queueFront(), qu.queueRear())

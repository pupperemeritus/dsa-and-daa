class Stack:
    def __init__(self, limit=100):
        self.stk = []
        self.limit = limit

    def push(self, data):
        if len(self.stk) < self.limit:
            self.stk.append(data)
        else:
            print("Stack Overflow")

    def pop(self):
        if len(self.stk) > 0:
            return self.stk.pop()
        else:
            print("Stack Underflow")

    def peek(self):
        if len(self.stk) > 0:
            return self.stk[-1]
        else:
            print("Empty Stack")

    def isEmpty(self):
        return len(self.stk) == 0


if __name__ == "__main__":
    st = Stack()
    for i in range(10):
        st.push(i)
    print(st.peek())
    print(st.pop())
    print(st.peek())

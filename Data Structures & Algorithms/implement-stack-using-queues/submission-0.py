"""
implement a stack using queues
stack is LIFO, q is FIFO

can only use push to back, peek/pop from front, size, and is empty 

have two queues, one to imitate the stack and the other to keep track of the order

stack = [1]

q = [1]
"""
class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.appendleft(x)

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return True if len(self.stack) == 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
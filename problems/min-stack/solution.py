class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.min = None


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._head = None

    def push(self, x: int) -> None:
        node = Node(x)
        node.min = x
        if self._head is not None:
            node.prev = self._head
            node.min = min(self._head.min, node.min)
        self._head = node

    def pop(self) -> None:
        self._head = self._head.prev if self._head is not None and self._head.prev is not None else None

    def top(self) -> int:
        return self._head.val

    def getMin(self) -> int:
        return self._head.min


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())

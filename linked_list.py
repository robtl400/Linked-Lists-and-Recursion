
class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        def helper(node):
            if node is None:
                return 0
            return node.data + helper(node.next)
        return helper(self.head)

    def recursive_reverse(self):
        def helper(prev, current):
            if current is None:
                return prev
            next_node = current.next
            current.next = prev
            return helper(current, next_node)
        self.head = helper(None, self.head)

    def recursive_search(self, target):
        def helper(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return helper(node.next)
        return helper(self.head)

    def display(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None" if elements else "None")

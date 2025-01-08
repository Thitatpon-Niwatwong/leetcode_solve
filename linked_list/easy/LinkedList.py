class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def display(self):
        current = self.head
        while current:
            print(current.value,end = "->")
            current = current.next
        print("None")

ll = LinkedList()
ll.push(1)
ll.display()  # Output: 1 -> 2 -> 3 -> None       

        
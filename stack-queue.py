# Case Study: Implementation of Stack and Queue Operations Using Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack Implementation Using Linked List
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed into Stack.")

    def pop(self):
        if self.top is None:
            print("Stack is empty!")
        else:
            print("Popped element:", self.top.data)
            self.top = self.top.next

    def display(self):
        if self.top is None:
            print("Stack is empty!")
            return

        current = self.top
        print("Stack elements (Top to Bottom):", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Queue Implementation Using Linked List
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(data, "inserted into Queue.")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty!")
            return

        print("Removed element:", self.front.data)
        self.front = self.front.next

        if self.front is None:
            self.rear = None

    def display(self):
        if self.front is None:
            print("Queue is empty!")
            return

        current = self.front
        print("Queue elements (Front to Rear):", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Main Program
stack = Stack()
queue = Queue()

while True:
    print("\n===== STACK AND QUEUE USING LINKED LIST =====")
    print("1. Push into Stack")
    print("2. Pop from Stack")
    print("3. Display Stack")
    print("4. Enqueue into Queue")
    print("5. Dequeue from Queue")
    print("6. Display Queue")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        data = input("Enter element to push: ")
        stack.push(data)

    elif choice == '2':
        stack.pop()

    elif choice == '3':
        stack.display()

    elif choice == '4':
        data = input("Enter element to enqueue: ")
        queue.enqueue(data)

    elif choice == '5':
        queue.dequeue()

    elif choice == '6':
        queue.display()

    elif choice == '7':
        print("Program exited successfully.")
        break

    else:
        print("Invalid choice! Please try again.")
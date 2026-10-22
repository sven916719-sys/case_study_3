# Case Study: Implementation of Stack and Queue Operations Using Linked Lists

## 1. Introduction
A Stack and a Queue are linear data structures used to store and manage data. In this case study, both data structures are implemented using a linked list in Python.

## 2. Objectives
- To implement Stack operations using a linked list.
- To implement Queue operations using a linked list.
- To understand the working of dynamic memory allocation.
- To perform insertion, deletion, and display operations.

## 3. Problem Statement
To develop a Python program that implements Stack and Queue operations using linked lists and allows users to perform operations through a menu-driven interface.

## 4. Data Structures Used

### Stack
A Stack follows the **LIFO (Last In, First Out)** principle. The element inserted last is removed first.

**Operations:**
- `Push`: Adds an element to the Stack.
- `Pop`: Removes the top element.
- `Display`: Shows all Stack elements.

### Queue
A Queue follows the **FIFO (First In, First Out)** principle. The element inserted first is removed first.

**Operations:**
- `Enqueue`: Adds an element to the rear of the Queue.
- `Dequeue`: Removes an element from the front.
- `Display`: Shows all Queue elements.

## 5. Algorithm

### Stack Algorithm
1. Create a Node class to store data and a link to the next node.
2. Initialize the top pointer as `None`.
3. For Push, insert a new node at the beginning.
4. For Pop, remove the node pointed to by top.
5. Display elements from top to bottom.

### Queue Algorithm
1. Initialize front and rear pointers as `None`.
2. For Enqueue, insert a new node at the rear.
3. For Dequeue, remove the node from the front.
4. If the Queue becomes empty, set rear to `None`.
5. Display elements from front to rear.

## 6. Technologies Used
- Programming Language: Python
- Concepts: Linked Lists, Stack, Queue, Classes and Objects
- Editor: Visual Studio Code

## 7. Applications
- **Stack:** Undo operations, browser history, function calls.
- **Queue:** Printer scheduling, task management, customer service systems.

## 8. Advantages
- Dynamic memory allocation.
- No fixed size is required.
- Efficient insertion and deletion.
- Stack and Queue operations are easy to implement.

## 9. Time Complexity

| Operation | Time Complexity |
|---|---|
| Stack Push | O(1) |
| Stack Pop | O(1) |
| Stack Display | O(n) |
| Queue Enqueue | O(1) |
| Queue Dequeue | O(1) |
| Queue Display | O(n) |

Here, `n` represents the number of elements.

## 10. Conclusion
This case study demonstrates the implementation of Stack and Queue operations using linked lists in Python. It helps in understanding LIFO and FIFO principles, node creation, pointer management, and efficient insertion and deletion operations.

## 11. How to Run the Program
1. Save the Python program as `stack_queue_linked_list.py`.
2. Open the terminal in VS Code.
3. Run the following command:

```bash
python stack_queue_linked_list.py
```

4. Select an option from the menu to perform Stack or Queue operations.

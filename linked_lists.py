from collections import deque
''' queue is a first in first out approach (FIFO) ie the first element in the  list is 
the first one to be retrieved

    stack is a last in first out approach (LIFO) ie the last element in the last is the first one
    to be retrieved

'''
print(deque(['a','b','c','d']))

llist = deque("abcde")
# append and pop remove elements from the right side of the linked list 
llist.append("h")

llist.pop()

# 
llist.appendleft("Q")

#llist.popleft()

print(llist)

# queue example FIFO
queue = deque()

queue.append("Uhtred")

queue.append("King Edward")

queue.append("Aethelflaed")

print(queue)

# remove the head element from the linked list with popleft()

queue.popleft()

print(queue)

# stacks example LIFO - think vertical

stack = deque()

stack.appendleft("item1")

stack.appendleft("item2")

stack.appendleft("item3")

print(stack)




class Node:
    def __init__(self, data):
        self.data = data
        # next contains a reference to the next node in the list
        self.next = None

    def __str__(self):
        return self.data




class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
         node = self.head
         nodes = []
         while node is not None:
             nodes.append(node.data)
             node = node.next
         nodes.append("None")
         return " -> ".join(nodes)
            
alist = LinkedList()

first_node = Node("a")
 
alist.head = first_node
print(alist)

second_node = Node("b")
third_node = Node("c")

first_node.next = second_node

second_node.next = third_node
print(alist)
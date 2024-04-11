## Testing linked lists code that I stole from the internet, playing around to see how things work,
## will probably delete things later.

#Singly Linked list implementation in Python


class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


if __name__ == '__main__':

    linked_list = LinkedList()

    # Assign item values
    # In my code, make it so you can dynamically assign values given the input being a list.
    linked_list.head = Node(1)    # Something like linked_list.head = Node(value of index 1)
    second = Node(2)     # second = Node (value of index 2)
    third = Node(3)    # third = Node (value of index 3)

    # Connect nodes
    linked_list.head.next = second
    second.next = third

    # Print the linked list item
    while linked_list.head != None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next


## Doubly linked list implementation in python
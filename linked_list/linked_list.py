
# Defines a node in the singly linked list
from tkinter import N


class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: 1
    # Space Complexity: 1
    def get_first(self):
        return (self.head.value if self.head else None)


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: 1
    # Space Complexity: 1
    def add_first(self, value):
        new_node = Node(value=value, next_node=self.head)
        self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: n
    # Space Complexity: 1
    def search(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: n
    # Space Complexity: 1
    def length(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: n
    # Space Complexity: 1
    def get_at_index(self, index):
        counter = 0
        node = self.head
        while node:
            if counter == index:
                return node.value
            counter += 1
            node = node.next
        return None


    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: n
    # Space Complexity: 1
    def get_last(self):
        node = self.head
        while node:
            if not node.next:
                return node.value
            else:
                node = node.next
        return None

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: n
    # Space Complexity: 1
    def add_last(self, value):
        node = self.head
        new_node = Node(value=value, next_node=None)
        if not node:
            self.head = new_node
        else:
            while node.next:
                node = node.next
            node.next = Node(value=value, next_node=None)

    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity: n
    # Space Complexity: 1
    def find_max(self):
        max = None
        node = self.head
        while node:
            if (max == None) or (node.value > max):
                max = node.value
            node = node.next
        return max

    # method to delete the first node found with specified value
    # Time Complexity: n
    # Space Complexity: 1
    def delete(self, value):
        node = self.head
        prev_node = None
        while node:
            if node.value == value:
                if prev_node:
                    prev_node.next = node.next
                else:
                    self.head = node.next
                return
            prev_node = node
            node = node.next

    # method to print all the values in the linked list
    # Time Complexity: n
    # Space Complexity: n
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: n
    # Space Complexity: 1
    def reverse(self):
        node = self.head
        prev_node = None
        while node:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            if not next_node:
                self.head = node
                return
            node = next_node

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: 2n => n
    # Space Complexity: 1
    def find_middle_value(self):
        middle_index = self.length() // 2
        return self.get_at_index(middle_index)

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: n
    # Space Complexity: 1
    def find_nth_from_end(self, n):
        index = self.length() - n - 1
        return self.get_at_index(index)

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: n
    # Space Complexity: n
    def has_cycle(self):
        visited_nodes = set()
        node = self.head
        while node:
            if node in visited_nodes:
                return True
            else:
                visited_nodes.add(node)
                node = node.next
        return False

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node


# Defines a node in the singly linked list
from email import header
from os import curdir
from socket import AI_PASSIVE


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
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head == None:
            return None
        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_head = Node(value, self.head)
        self.head = new_head

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: ?
    # Space Complexity: ?
    def search(self, value):
        cur = self.head
        while cur != None:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def length(self):
        cur = self.head
        i = 0
        while cur != None:
            cur = cur.next
            i += 1
        return i

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: ?
    # Space Complexity: ?
    def get_at_index(self, index):
        cur = self.head
        for i in range(index):
            if cur == None:
                return None
            cur = cur.next
        return cur.value


    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: ?
    # Space Complexity: ?
    def get_last(self):
        if self.head == None:
            return None
        cur = self.head
        prev = None
        while cur != None:
            prev = cur
            cur = cur.next
        return prev.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def add_last(self, value):
        if self.head == None:
            self.head = Node(value, None)
            return
        cur = self.head
        prev = None
        while cur != None:
            prev = cur
            cur = cur.next
        prev.next = Node(value, None)


    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if self.head == None:
            return None
        cur = self.head
        cur_max = cur.value
        cur = cur.next
        while cur != None:
            if cur.value > cur_max:
                cur_max = cur.value
            cur = cur.next
        return cur_max


    # method to delete the first node found with specified value
    # Time Complexity: ?
    # Space Complexity: ?
    def delete(self, value):
        if self.head == None:
            return None
        if self.head.value == value:
            self.head = self.head.next
        
        prev = self.head
        cur = self.head.next
        while cur != None and cur.value != value:
            prev = cur
            cur = cur.next
        
        if cur != None:
            prev.next = cur.next



    # method to print all the values in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: ?
    # Space Complexity: ?
    def reverse(self):
        cur = self.head
        last_made = None
        while cur != None:
            last_made = Node(cur.value, last_made)
            cur = cur.next
        self.head = last_made
  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def find_middle_value(self):
        pass

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        pass

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        pass

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

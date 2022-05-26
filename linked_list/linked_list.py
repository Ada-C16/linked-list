
# Defines a node in the singly linked list
from operator import truediv

class Node:

    def __init__(self, value, next_node = None, previous_node = None):
        self.value = value
        self.next = next_node
        self.previous = previous_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: ? O(1)
    # Space Complexity: ? O(1)
    def get_first(self):
        if self.head == None:
            return self.head
        else:
            return self.head.value

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: ? O(1)
    # Space Complexity: ? O(1)
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: ? 
    # Space Complexity: ?
    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def length(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
        return count

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: ?
    # Space Complexity: ?
    def get_at_index(self, index):
        i = 0
        current = self.head
        while current:
            if i == index:
                return current.value 
            current = current.next
            i += 1
        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: ?
    # Space Complexity: ?
    def get_last(self):
        if not self.head:
            return None
        current = self.head
        while current:
            if not current.next:
                return current.value
            current = current.next   

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: ? O(1)
    # Space Complexity: ? O(1)
    def add_last(self, value):
        if not self.head:
            self.head = Node(value)
            return

        current = self.head
        # get to the last value in the list
        while current:
            if not current.next: #if we're at the last node of the list thennnn
                # add a new node to the end 
                current.next = Node(value)
                return 
            current = current.next

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        # check is the list is empty
        if not self.head:
            return None
        # create a varible max_value 
        max_value = 0
        # and variable current starting at the head
        current = self.head
        # iterate current through from head to last node (for the last node current.next will be falsy None)
        while current:
        # compare each current node's value with max_value and update max value if current.value is greater than it
            if current.value > max_value:
                max_value = current.value
            current = current.next
        # return the max value
        return max_value

    # method to delete the first node found with specified value
    # Time Complexity: ? O(1)
    # Space Complexity: ? O(1)
    def delete(self, value):
        pass
        # check that the list isn't empty, if it is return none
        if not self.head:
            return None

        #if the head matched make .next the head
        if self.head.value == value:
            self.head = self.head.next
            return
        # iterate thru the list until a node's value == the given value
        previous = self.head
        current = self.head.next
        while current:
            if current.value == value:
                previous.next = current.next
                return
            previous = current
            current = current.next
        # point the previous node to skip over the matching node and point to the matching mode's .next value
        # if the matching value is the head, resign self.head to the next value. 
        # if there is no next value return None
        # if theres so match return None

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

        if not self.head:
            return None

        previous = None
        current = self.head
        next_node = None

        # make the list doubly linked by adding real values to .previous
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous


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
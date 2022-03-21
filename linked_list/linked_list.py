
# Defines a node in the singly linked list
from tkinter.messagebox import NO


class Node:

    def __init__(self, value, next_node=None, previous_node=None):
        self.value = value
        self.next = next_node
        self.previous = previous_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class
        self.tail = None

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head is None:
            return None
        else:
            return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            new_node = Node(value, self.head)
            self.head.previous = new_node
            self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        if self.head is None:
            return False

        # # Traverse the list until you find the node at index -1
        current = self.head
        while current:
            if current.next is None:
                if current.value == value:
                    return True
                else:
                    return False
            elif current.value == value:
                return True
            else:
                current = current.next
        return False
    

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        counter = 0

        if self.head == None:
            return 0
        current = self.head
        while current is not None:
            counter += 1
            current = current.next 
        return counter


    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        counter = 0
        
        if self.head == None:
            return None

        current = self.head
        while current is not None:
            if counter == index:
                return current.value
            else:
                current = current.next
                counter += 1


    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        current = self.head

        while current:
            if current.next is None:
                return current.value
            else:
                current = current.next


    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_last(self, value):
        if self.tail is None:
            self.tail = self.head = Node(value)
        else:
            new_node = Node(value, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node


    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_max(self):
        max_val = 0

        if self.head == None:
            max_val = None
        current = self.head
        while current is not None:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val

    # method to delete the first node found with specified value
    # Time Complexity: ?
    # Space Complexity: ?
    def delete(self, value):
        if self.head == None:
            return None

        current = self.head
        prev_node = current.previous
        next_node = current.next

        while current:
            if current.value == value:
                if prev_node == None:
                    next_node.previous = None
                    self.head = next_node
                    current = None
                elif next_node == None:
                    prev_node.next = None
                    self.tail = prev_node
                else:
                    prev_node.next = next_node
                    next_node.previous = prev_node
            else:
                current = current.next
                

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
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):

        if self.head == self.tail:
            return None
        
        
        current = self.head

        while current is not None:
            prev = current.previous
            next = current.next
            current.next = prev
            current.previous = next
            current = next

        temp_head = self.head
        self.head = self.tail
        self.tail = temp_head





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

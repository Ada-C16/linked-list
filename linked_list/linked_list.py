
# Defines a node in the singly linked list
from requests import head


class Node:

    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next = next_node
        self.previous = prev_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class
        self.tail = None

    #----------------------
    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1) 
    # Space Complexity: O(1)
    def get_first(self):
        if self.head:
            return self.head.value
        return None

    #----------------------
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

    #----------------------
    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current = self.head
        if current == None:
            return False
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    #----------------------
    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        counter = 0
        current = self.head

        while current != None:
            current = current.next
            counter +=1
        return counter

    #----------------------
    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        counter = 0
        current = self.head

        while current != None:
            if counter == index:
                return current.value
            counter += 1 
            current = current.next
        return None

    #----------------------
    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        current = self.head
        if current == None:
            return None

        while current.next != None:
            current = current.next
        return current.value

    #----------------------
    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        if self.head == None:
            self.add_first(value)
        
        else:    
            new_node = Node(value)
            current = self.head

            while current.next:
                current = current.next
            current.next = new_node

    #----------------------
    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        max_value = 0
        if self.head == None:
            return None
        
        current  = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
            
        return max_value

    #----------------------
    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        current = self.head
        
        if current == None:
            return 
        
        while current:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                    self.head.previous = None
                    return
                
                if current == self.tail:
                    self.tail = current.previous
                    self.tail.next = None
                    return

                current.previous.next = current.next
                current.next.previous = current.previous
                return
            current = current.next

    #----------------------
    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    #----------------------
    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        if not self.head:
            return
        
        current_node = self.head
        previous_node = None
        
        while current_node:
            next = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next
        
        self.head = previous_node
            

    #---------------------- Advanced/ Exercises -----------------------
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        mid_value = int(self.length() / 2)
        return self.get_at_index(mid_value)

    #----------------------
    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        nth_from_end = self.length() - (n+1)
        return self.get_at_index(nth_from_end)

    #----------------------    
    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
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

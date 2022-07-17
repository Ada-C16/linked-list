
# Defines a node in the singly linked list
# from ast import Pass


class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node
        # self.previous = previous_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None 
        # keep the head private. Not accessible outside this class
        # self.length = 0 # keep the length private. Not accessible outside this class
        # if self.head == None:
        #     self.head = Node(None)
        #     self.length = 0
        # else:
        #     self.length = 1

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):

        if self.head == None:
            return None
        else: 
            return self.head.value

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):

        if self.head == None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return self.head

        # if self.head == None:
        #     return None 

        # self.head = Node(value, self.head)
        # self.length += 1
        # return self.head

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def search(self, value):
        if self.head == None:
            return None

        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):

        length_counter = 0
        current = self.head
        while (current != None):
            length_counter += 1
            current = current.next

        return length_counter


    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):

        if self.head == None:
            return None 

        if self.length() < index:
            return None

        current_value = 0 
        current_node = self.head
        while current_value:
            current_node = current_node.next
            current_value += 1

        return current_node.value
        

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if self.head == None:
            return None

        current = self.head
        while current.next:
            current = current.next
        return current.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_last(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
            
            return self.head

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if self.head == None:
            return None

        current = self.head
        max_value = current.value
        while current != None:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        
        if self.head == None:
            return None

        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous == None:
                    self.head = current.next
                    return
                else:
                    previous.next = current.next
                    return
            else:
                previous = current
                current = current.next
        
        return None

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
        if self.head == None:
            return None

        previous = None
        current = self.head

        while current != None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous
        return previous
  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def find_middle_value(self):
        if self.head == None:
            return None

        current = self.head
        middle_value = None
        for i in range(self.length // 2):
            current = current.next
            middle_value = current.value
        
        return middle_value

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        if self.head == None:
            return None
        
        current = self.head
        for i in range(n):
            current = current.next

        return current.value

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        if self.head == None:
            return None

        current = self.head
        visited = []
        while current:
            if current in visited: 
                return True
            else:
                visited.append(current)
                current = current.next
        return False

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return None

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node

        return self.head

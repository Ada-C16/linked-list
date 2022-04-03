
# Defines a node in the singly linked list
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
        if not self.head:
            return None
        else:
            return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        node_to_add = Node(value)
        node_to_add.next = self.head
        self.head = node_to_add

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        length = 0
        current_node = self.head
        while current_node:
            length += 1 
            current_node = current_node.next
        return length

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        i = 0 
        current_node = self.head
        while current_node:
            if i == index:
                return current_node.value
            i += 1
            current_node = current_node.next
        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if not self.head:
            return None
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        return current_node.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        if not self.head:
            self.head = Node(value)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(value)

    # method to return the max value in the linked list
    # returns the data value and not the node
    # Note: assuming linked list values are only positive numbers or zeroes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_max(self):
        max = 0
        if not self.head:
            return None
        current_node = self.head
        while current_node:
            if current_node.value > max:
                max = current_node.value
            current_node = current_node.next
        return max

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        current_node = self.head
        prev_node = None
        if not current_node:
            return None
        if current_node.value == value:
            self.head = current_node.next
            return
        while current_node:
            if current_node.value == value:
                prev_node.next = current_node.next
                return
            prev_node = current_node    
            current_node = current_node.next

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
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
        # if list is empty or one long, do nothing
        if not self.head or not self.head.next:
            return 
        if self.length() == 2:
            second_node = self.head.next
            self.head.next = None
            second_node.next = self.head
            self.head = second_node
            return

        prev_node = self.head
        current_node = self.head.next
        next_node = current_node.next
        while next_node:
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            next_node = next_node.next
        current_node.next = prev_node
        self.head.next = None
        self.head = current_node
        
  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        middle = self.length() // 2
        return self.get_at_index(middle)

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        length = self.length()
        return self.get_at_index(length - 1 - n)

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def has_cycle(self):
        node_map = {}
        current_node = self.head
        while current_node:
            if node_map.get(current_node):
                return True
            node_map[current_node] = True
            current_node = current_node.next
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

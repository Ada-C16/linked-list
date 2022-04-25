
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
        return self.head.value if self.head else None

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, target_value):
        if not self.head:
            return False
        current = self.head
        while current and current.value != target_value:
            current = current.next
        return current != None     

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        if not self.head:
            return 0
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        length = self.length() #O(n)
        if index >= length:
            return None
        current = self.head
        current_index = 0
        while current_index < index:
            current = current.next
            current_index += 1
        return current.value

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if not self.head:
            return None
        current = self.head
        while current.next:
            current = current.next
        return current.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # method to return the max value in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # returns the data value and not the node
    def find_max(self):
        if not self.head:
            return None
        current = self.head
        max_val = self.head.value
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val


    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, target):
        if not self.head:
            return None
        if self.head.value == target:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == target:
                current.next = current.next.next
            else:
                current = current.next
        # while current and current.value != target:
        #     previous_node = current
        #     current = current.next
        # if not current:
        #     return None #raise error, node not found
        # previous_node.next = current.next

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
        # first node will have no next
        # second node's next will be the first node
        # third node's next will be the second node and so on

        # iterative solution:
        if not self.head:
            return None # error for empty LL
        previous = None
        current = self.head
        while current:
            nxt = current.next # this node's original next
            current.next = previous # this node's original previous
            previous = current # next node's previous
            current = nxt # go to saved node
        self.head = previous

  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        list_len = self.length() # O(1)
        tar_ind = list_len // 2
        curr_ind = 0
        current = self.head
        while curr_ind != tar_ind:
            curr_ind += 1
            current = current.next
        return current.value

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        if self.head is None:
            return None
        length = self.length() # O(n)
        target_position = length - n
        if target_position < 0:
            return None
        position = 1
        current = self.head
        while current and position != target_position:
            current = current.next
            position += 1
        if current == None:
            return None
        return current.value

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def has_cycle(self):
        # keep track of all of the current nodes?
        # if we arrive somewhere where current.next equals a node in our list, return true
        # can I make an array of nodes?
        # or a dictionary/hashmap?
        if not self.head:
            return False
        current = self.head
        freq_map = {}
        while current:
            if current in freq_map:
                return True
            freq_map[current] = 1
            current = current.next
        return False
        # works, but how can I solve this with constant memory


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


# # TO DO:
# optimize has_cycle for constant memory 
# optimize find_middle
# recursive solution for reverse LL

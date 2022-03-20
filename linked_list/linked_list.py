
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class
        self.tail = None
    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: n/a
    def get_first(self):
        if self.head is None: # 1
            return None 
        return self.head.value

    
    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value, self.head)
        if self.head == None: #  1
            self.tail = new_node
        self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current = self.head
        if current is None: # 1
            return False
        while current is not None: # n
            if current.value == value: # 1
                return True 
            current = current.next 
        return False


    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        ctr = 0
        current = self.head
        while current is not None:
            ctr += 1
            current = current.next

        return ctr

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        ctr = 0
        current = self.head
        while current is not None:
            if ctr == index:
                return current.value
            ctr += 1
            current = current.next
        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1) ?
    def get_last(self):
        if self.head is None:
            return None
        return self.tail.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        current = self.head
        if self.head is None:
            self.add_first(value)
            return
        while current.next is not None:
            current = current.next
        current.next = Node(value)
        self.tail = current.next
        

    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_max(self):
        if self.head is None:
            return None
        high = self.head.value
        current = self.head
        while current is not None:
            if current.value > high:
                high = current.value
            current = current.next
        return high

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):

        current = self.head
        if current is None:
            return

        # head
        if current.value == value:
            self.head = current.next
            return 
        # middle
        while current.next is not None:
            if current.value == value:
                current.next = current.next.next
                return
            prev = current
            current = current.next
        # tail
        if current.value == value:
            prev.next = None
            self.tail = prev

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


    def delete_last(self):
        # empty
        if self.head is None:
            return
        # one element
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        # multiple
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        self.tail = current

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n^2)
    # Space Complexity: size of linkedList object O(n)?
    def reverse(self):
        import copy
        current = copy.deepcopy(self) # O(n)? how big is LinkedList() object
        self.head = None
        self.tail = None


        while current.head is not None: #:weary:
            self.add_last(current.get_last())
            current.delete_last()
  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(2n) - O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        k = self.length() // 2
        current = self.head
        for i in range(k):
            current = current.next
        return current.value


    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n^2)
    # Space Complexity: size of linkedList object O(n)?
    def find_nth_from_end(self, n):
        if n >= self.length(): # O(n)
            return None
        
        import copy
        copy = copy.deepcopy(self)
        for i in range(n): #O(n)
            copy.delete_last() # O(n)
        return copy.tail.value

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def has_cycle(self):
        if self.head is None:
            return False
        nodes = {self.head}
        current = self.head
        while current.next is not None:
            if current.next in nodes:
                return True
            nodes.add(current.next)
            current = current.next
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

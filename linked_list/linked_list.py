
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
        if self.head:
            return self.head.value
        else:
            return None

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        if self.head == None:
            new_node = Node(value)
        else:
            new_node = Node(value, next_node=self.head)
        self.head = new_node
        return new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        if self.head == None:
            return False

        current = self.head

        while current != None:
            if current.value == value:
                return True
            current = current.next

        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        current = self.head

        length = 0

        while current != None:
            length += 1
            current = current.next

        return length

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        if self.length() < index:
            return None
        
        else:
            current = self.head
            i = 0

            while i != index:
                current = current.next
                i += 1

            return current.value

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if self.head == None:
            return None
        
        current = self.head

        while current.next != None:
            current = current.next
        
        return current.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        if self.head == None:
            self.add_first(value)
            return
        
        current = self.head
        
        while current.next != None:
            current = current.next
        
        current.next = Node(value)

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if self.length() == 0:
            return None

        max_value = 0
        max_value_node = 0
        current = self.head

        while current != None:
            if current.value > max_value:
                max_value = current.value
                max_value_node = current
            current = current.next

        return max_value_node.value

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        if self.length() == 0:
            return None
        
        elif self.head.value == value:
            self.head = self.head.next

        else:
            current = self.head
            previous_node = None

            while current.value != value:
                if current.next.value == value:
                    current.next = current.next.next
                    return
                else:
                    previous_node = current
                    current = current.next

            previous_node.next = None

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
    # Time Complexity: 
    # Space Complexity: ?
    def reverse(self):
        
        length = self.length()
        current = None

        for i in range(length-1):
            is_last = self.head
            previous = None
            while is_last.next != None:
                previous = is_last
                is_last = is_last.next
            if i == 0:
                is_last.next = self.head
                self.head = is_last
                previous.next = None
                current = is_last
            else:
                is_last.next = current.next
                current.next = is_last
                previous.next = None
                current = is_last


    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        length = self.length()

        current = self.head 

        midpoint = length // 2

        return self.get_at_index(midpoint)

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        
        if self.length() <= n:
            return None

        self.reverse()
        current = self.head

        for i in range(n):
            current = current.next
        
        self.reverse()

        return current.value

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        if not self.head:
            return False

        current = self.head
        nodes = {}

        while current.next != None:
            if current.next not in nodes:
                nodes[current] = True
                current = current.next
            else:
                return True
        
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

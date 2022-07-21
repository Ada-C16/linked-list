
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
        
        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        added = Node(value)
        added.next = self.head
        self.head = added

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        len = 0
        curr = self.head
        while curr:
            len += 1
            curr = curr.next
        return len


    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        i = 0
        curr = self.head
        while curr:
            if i == index:
                return curr.value
            i += 1
            curr = curr.next

        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if not self.head:
            return None
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        if not self.head:
            self.head = Node(value)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(value)

    # method to return the max value in the linked list
    # returns the data value and not the node
    #Time Complexity: O(n)
    #Space Complexity: O(1)
    def find_max(self):
        max = 0
        if not self.head:
            return None
        curr = self.head
        while curr:
            if curr.value > max:
                max = curr.value
            curr = curr.next
        return max

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        curr = self.head
        prev = None
        if not curr:
            return None
        if curr.value == value:
            self.head = curr.next
            return 
        while curr:
            if curr.value == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

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
        if not self.head or not self.head.next:
            return
        if self.length() == 2:
            second = self.head.next
            self.head.next = None
            second.next = self.head
            self.head = second
            return

        prev = self.head
        curr = self.head.next
        next = curr.next
        while next:
            curr.next = prev
            prev = curr
            curr = next
            next = next.next
        curr.next = prev
        self.head.next = None
        self.head = curr

    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        mid = self.length() // 2
        return self.get_at_index(mid)

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        len = self.length()
        return self.get_at_index(len - 1 - n)

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def has_cycle(self):
        node_map = {}
        curr = self.head
        while curr:
            if node_map.get(curr):
                return True
            node_map[curr] = True
            curr = curr.next
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

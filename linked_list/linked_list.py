
# Defines a node in the singly linked list

class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
# Starting off a linked list is always constant time and space complexity.
class LinkedList:
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if self.head is None:
            return None
        
        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        # more compact, not as readable, need to look at the constructor to understand
        # self.head references the original linked list that the new head is assigned to
        # self.head = Node(value, self.head)


    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        # initialize a node pointer
        current = self.head

        while current != None:
            if current.value == value:
                return True  # Value was found
            
            current = current.next

        return False  # Value not found

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        pointer = self.head
        counter = 0

        while pointer != None:
            counter += 1
            pointer = pointer.next

        return counter

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: 0(1)
    def get_at_index(self, index):
        if index < 0:
            return None

        current_index = 0
        pointer = self.head

        while pointer != None:
            if current_index == index:
                return pointer.value
            pointer = pointer.next
            current_index += 1

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        # pointer = self.head
        # next_node = pointer.next

        # while next_node != None:
        #     pointer = next_node
        #     next_node = pointer.next

        if self.head is None:
            return None
        
        pointer = self.head
        
        while pointer.next is not None:
            pointer = pointer.next
            
        return pointer.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if self.head is None:
            return None

        pointer = self.head
        maximum = self.head.value

        while pointer is not None:
            if maximum < pointer.value:
                maximum = pointer.value
            pointer = pointer.next
        
        return maximum


    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        position = self.head

        if position is not None:
            if position.value == value:
                self.head = position.next
                position = None
                return

        while position is not None:
            if position.value == value:
                break
            prev = position
            position = position.next

        if position == None:
            return

        prev.next = position.next
        position = None

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
        prev = None
        current = self.head
        next_node = current.next

        while current:
            current.next = prev
            prev = current
            current = next_node
            if next_node:
                next_node = next_node.next

        self.head = prev

# ======================================================================================

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

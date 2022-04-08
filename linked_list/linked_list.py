
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

        # another way to do:
        # self.head = Node(value, self.head)

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
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
        if index < 0:
            return None
        
        current_index = 0
        current = self.head

        while current is not None and current_index < index:
            current = current.next
            current_index += 1
            
        if current is None:
            return None

        return current.value

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):        
        current_value = 0
        current = self.head

        if current == None:
            return current
        
        while current is not None:
            current_value = current.value
            current = current.next
            
        return current_value
        
        

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        last_node = self.head
        if not last_node:
            last_node = Node(value)
            self.head = last_node
        else:
            while last_node.next:
                last_node = last_node.next
            last_node.next = Node(value)

        return self

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        current = self.head
        if not current:
            return None
        max = 0

        while current:
            if current.value > max:
                max = current.value
            current = current.next
        
        return max

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        current = self.head
        if not current:
            return None
        previous = None
        next = None

        while current:
            if not previous and current.value == value:
                next = current.next
                self.head = next
                return self
            elif current.next is None and current.value == value:
                previous.next = None
                return self
            elif current.value == value:
                previous.next = current.next

            previous = current
            current = current.next

        return self

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
        current = self.head
        previous = None
        next = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        
        self.head = previous
  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        mid_point = self.length() // 2
        middle_value = self.get_at_index(mid_point)
        return middle_value


    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        length = self.length()
        if length == 0 or n > length:
            return None
        else:
            index_to_find = length - (n+1)
            value = self.get_at_index(index_to_find)
            return value

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def has_cycle(self):
        visited_nodes = []
        current = self.head
        
        while current is not None:
            visited_nodes.append(current)
            if current.next in visited_nodes:
                return True
            else:
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

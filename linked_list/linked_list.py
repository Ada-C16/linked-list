
# Defines a node in the doubly linked list
class Node:

    def __init__(self, value, next_node = None, previous_node = None):
        self.value = value
        self.next = next_node
        self.prev = previous_node

# Defines the doubly linked list
class LinkedList:
    def __init__(self):
        self.__head = None # keep the head private. Not accessible outside this class
        self.__tail = None

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)  
    def get_first(self):
        if self.__head == None:
            return

        return self.__head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        node = Node(value)

        if self.__head == None: 
            self.__head = self.__tail = Node(value)
        else: 
            temp = self.__head
            self.__head.prev = node
            self.__head = node
            self.__head.next = temp

    
    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        if self.__head == None:
            return False

        current = self.__head

        if current.value == value: 
            return True

        while current.next: 
            current = current.next
            if current.value == value:
                return True
        
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        if self.__head == None: 
            return 0
        
        current = self.__head
        length = 1

        while current.next:
            length += 1
            current = current.next

        return length

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        length = self.length()
        current = self.__head
        current_index = 0

        if index > (length - 1) or self.__head == None:
            return None

        while current_index < index: 
            current = current.next
            current_index += 1

        return current.value


    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_last(self):
        if self.__tail == None: 
            return None
        
        return self.__tail.value

    # method that inserts a given valaue as a new last node in the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_last(self, value):
        node = Node(value)

        if self.__tail == None: 
            self.__head = self.__tail = node
        else: 
            temp = self.__tail
            self.__tail.next = node
            self.__tail = node
            self.__tail.prev = temp

    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_max(self):
        if self.__head == None: 
            return None

        current = self.__head
        max = current.value

        while current.next: 
            if current.next.value > max:
                max = current.next.value
            current = current.next

        return max 

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        if self.__head == None: 
            return None

        current = self.__head 

        if current.value == value: 
            self.__head = self.__head.next
            self.__head.prev = None

        if self.__tail.value == value:
            self.__tail = self.__tail.prev
            self.__tail.next = None

        while current.next: 
            if current.next.value == value: 
                current.next = current.next.next
                current.next.prev = current
            
            current = current.next


    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def visit(self):
        helper_list = []
        current = self.__head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        if self.__head == None: 
            return None

        if self.__head == self.__tail: 
            return self.__head

        current = self.__head

        while current != None: 
            prev = current.prev
            next = current.next
            current.next = prev
            current.prev = next
            current = next

        temp = self.__head
        self.__head = self.__tail
        self.__tail = temp   
            
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        if self.__head == None: 
            return None

        if self.__head == self.__tail: 
            return self.__head

        left = self.__head
        left_index = 0
        right = self.__tail
        right_index = (self.length() - 1)

        while left_index < right_index: 
            left = left.next 
            left_index += 1

            right = right.prev
            right_index -= 1

        return left.value
        

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        if self.__head == None: 
            return None

        n_from_head = ((self.length() - 1) - n)

        if n_from_head < 0: 
            return None

        index = 0
        current = self.__head

        while index < n_from_head: 
            current = current.next
            index += 1

        return current.value

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        linked_list_set = set()

        current = self.__head

        while current: 
            if current in linked_list_set:
                return True

            linked_list_set.add(current)

            current = current.next

        return False 

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.__head == None:
            return

        # navigate to last node
        current = self.__head
        while current.next != None:
            current = current.next

        current.next = self.__head # make the last node link to first node


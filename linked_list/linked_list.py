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
    # Time Complexity: Linear O(N), size of LL
    # Space Complexity: Constant O(1)
    def get_first(self):
        if self.head is None:
            return None 

        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: Adding a head, Constant O(1)
    # Space Complexity: Constant O(1) not creating new data structure
    def add_first(self, value):
        # new_node = Node(value)
        # new_node.next = self.head
        # self.head = new_node

        self.head = Node(value, self.head)

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: Linear O(N), size of the LL
    # Space Complexity: Constant O(1), we're not creating data structures
    def search(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False        
            
    # method that returns the length of the singly linked list
    # Time Complexity: Linear O(N), size of the LL
    # Space Complexity: Constant O(1), we're not creating data structures
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next

        return count

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: Linear O(N), size of the LL
    # Space Complexity: Constant O(1), we're not creating data structures
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
    # Time Complexity: Linear O(N), size of the LL
    # Space Complexity: Constant O(1), we're not creating data structures
    def get_last(self):
        if not self.head:
            return None
        
        current = self.head
        while current.next:
            current = current.next

        return current.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: Linear O(N), size of the LL
    # Space Complexity: Constant O(1), we're not creating data structures
    def add_last(self, value):
        if not self.head:
            self.add_first(value)
        else:
            new_node = Node(value)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node 

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if self.head == None:
            return None

        current = self.head
        max = self.head.value
        while current:
            if current.value > max:
                max = current.value
            current = current.next

        return max

    # method to delete the first node found with specified value
    # Time Complexity: Linear O(N), size of the LL
    # Space Complexity: Constant O(1), we're not creating data structures
    def delete(self, value):
        if not self.head:
            return -1
        elif self.head.value == value:
            self.head = self.head.next
            return True
        else:
            current = self.head
            while current.next and current.next.value != value:
                current = current.next
            current.next = current.next.next

    # method to print all the values in the linked list
    # Time Complexity: Linear O(N), size of the LL
    # Space Complexity: Linear O(N), depending on the size of the visited_list
    def visit(self):
        visited_list = []
        current = self.head

        while current:
            visited_list.append(str(current.value))
            current = current.next
        
        print(", ".join(visited_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: Linear O(N), depending on the size of the LL
    # Space Complexity: Constant O(1), no creation of new data structures
    def reverse(self):
        if not self.head:
            return -1

        current = self.head
        previous = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        self.head = previous
  
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


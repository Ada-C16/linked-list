
# Defines a node in the singly linked list
from calendar import c


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
    # Time Complexity: ?
    # Space Complexity: ?
    def get_first(self):
        if self.head:
            return self.head.value
        return None
        


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: o(1)
    # Space Complexity: o(1)
    def add_first(self, value):
        self.head = Node(value, self.head)
        
      

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: o(n)
    # Space Complexity: o(1)
    def search(self, value):
        if not self.head:
            return False
        if self.head.value == value:
            return True

        current = self.head
        while current.next:
            if current.next.value == value:
                return True
            current = current.next
        
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity:    O(1)
    def length(self):
        if not self.head:
            return 0
        
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity:   o(1)
    def get_at_index(self, index):
        if self.length() <= index:
            return None

        current = self.head
        count = 0

        while current:
            if count == index:
                return current.value
            count += 1
            current = current.next
        return None 

        

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: o(n)
    # Space Complexity: o(1)
    def get_last(self):
        if not self.head:
            return None
        current = self.head 
        while current.next:
            current = current.next
        return current.value 
        # return self.tail.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: o(n)
    # Space Complexity: o(1)
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
        if not self.head: 
            return None 
        current = self.head
        max = current.value

        while current: 
            if max < current.value: 
                max = current.value 
            current = current.next
        return max

    # method to delete the first node found with specified value
    # Time Complexity: o(n)
    # Space Complexity: o(1)
    def delete(self, value):
        if not self.head: 
            return 
        # current = self.head 
        elif current.value == value:
            self.head = current.next
            return True 
        else:
            current = self.head 
            while current.next and current.next.value != value: 
                current = current.next 
            current.next = current.next.next
            # if self.head:
            #     self.head.previous = None
            # if not self.head:
            #     self.tail = None    
            # return None 

        #   previous = current

        # while current.next:
        #     if current.next.value == value:
        #         current.next = current.next.next
        #         if current.next:
        #             current.next.previous = current
        #         if not current.next:
        #             self.tail = current

        #         return None
         


    # method to print all the values in the linked list
    # Time Complexity: o(n)
    # Space Complexity: o(1)            
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
        if not self.head: 
            return None

        prev = None
        current = self.head

        while current: 
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        temp =self.head 
        count = 0
        while self.head: 
            count += 1
            self.head = self.head.next
        self.head = temp
        if count % 2 == 0:
            return self.get_at_index(count//2)
        else:
            return self.get_at_index(count//2 + 1)   # return the value at the middle index
    # Time Complexity: O(n)

    # Space Complexity: O(1)

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: o(n)
    # Space Complexity: o(1)
    def find_nth_from_end(self, n):
        i = 0
        if not self.head:
            return None 
        return self.get_at_index(self.length() - n - 1)
      
    # Time Complexity: O(n)

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        # curr = head 
        s = set() 
        while curr:
            if curr in s:
                return True
            s.add(curr)
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

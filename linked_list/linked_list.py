
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
    # Space Complexity: O(1)
    def get_first(self):
        if self.head == None:
            return None
        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        if self.head == None:
            self.head = self.tail = Node(value)
        else:
            temp = self.head
            new_node =  Node(value, temp)
            # new_node.next = temp
            self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        if self.head == None:
            return False
        
        pointer = self.head
        while pointer is not None:
            if pointer.value == value:
                return True
            pointer = pointer.next

        return False



    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        if self.head == None:
            return 0
        su = 0
        pointer = self.head
        while pointer is not None:
            su += 1
            pointer = pointer.next
           
        return su 


    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        if self.head == None:
            return None
        pointer = self.head
        count = 0
        while pointer is not None:
            if count == index:
                return pointer.value
            pointer = pointer.next
            count +=1 
        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_last(self):
       if self.tail == None:
           return None
       return self.tail.value
        

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_last(self, value):
        if self.tail == None:
            self.head = self.tail = Node(value)
        new_node = Node(value)
        self.tail.next = new_node
        new_node.next = None
        self.tail = new_node
        

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
       if self.head == None:
           return None
       max = -99999999
       pointer = self.head
       while pointer is not None:
           if pointer.value > max:
               max = pointer.value
           pointer = pointer.next
       return max

    # method to delete the first node found with specified value
    # Time Complexity: ?
    # Space Complexity: ?
    def delete(self, value):
        pointer = self.head
        previous = None
        while pointer is not None:
            if pointer.value == value:
                previous = pointer.next
                pointer = None
            else:
                pointer = pointer.next
                previous = pointer 
           
     

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
    # Time Complexity: ?
    # Space Complexity: ?
    def reverse(self):
        pass
  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
       if self.head == None:
           return None
       mid = self.length()//2
       index = 0
       pointer = self.head
       while pointer:
           if index == mid:
               return pointer.value
           index += 1
           pointer = pointer.next



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

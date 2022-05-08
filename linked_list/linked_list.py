
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None,previous = None):
        self.value = value
        self.next = next_node
        self.previous = previous

# Defines the singly linked list
class LinkedList:
    def __init__(self):
      self.head = None # keep the head private. Not accessible outside this class
    #   self.tail = None
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
            self.head = Node(value)
        else:
            new_node=Node(value)
            new_node.next=self.head
            self.head=new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        node=self.head
        while node:
            if self.head.value==value:
                return True
            node=self.head.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: ?
    def length(self):
        counter=0
        node=self.head
        while node:
            counter+=1
            node=self.head.next
        return counter


    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        if self.length()<index:
            return None
        counter=0
        node=self.head
        while node:
            if counter==index:
                return self.head.value
            node=self.head.next
            counter+=1
        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if self.length()==0:
            return None
        counter=0
        node=self.head
        while node:
            counter+=1
            if self.head.next == None:
                tail=Node(self.head)
                return tail.value
        return None
        

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        if self.length()==0:
            self.add_first()
        else:
            counter=0
            node=self.head
            while node:
                counter+=1
                if self.head.next == None:
                    break
            self.head.next=Node(value)

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        
        node=self.head
        max=self.head.value
        while node:
            if self.head.value>max:
                max=self.head.value
            node=node.next
        return max
            

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        if self.search(value):
            node=self.head
            while node:
                if self.get_first()==value:
                    self.head.next=None
                elif self.head.value==value:
                    self.head.next=None
                    self.head.previous=None


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
        current_node=self.head
        previous=None

        while current_node:
            next = self.head.next
            current_node.next = previous
            previous = current_node
            current_node = next
        
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

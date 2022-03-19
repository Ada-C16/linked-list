
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
        new_node = Node(value) # make the node 
        new_node.next = self.head # make the next of new_node the current head
        self.head = new_node # assign the head position to the newly-made node

        return self.head.value 
        

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
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
        counter = 0

        while current != None:
            counter += 1
            current = current.next 

        return counter 

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        idx_counter = 0

        current = self.head 
        while current != None:
            if idx_counter == index:
                return current.value 
            idx_counter += 1
            current = current.next 

        return None 

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        current = self.head 

        # return None for empty list 
        if not current:
            return None 

        # keep looping until you reach the end of the links 
        while current.next:
            current = current.next 

        # return the value at the end 
        return current.value 


    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        current = self.head 
        new_node = Node(value)

        # if list is empty, set new_node to head and return 
        if not current:
            self.head = new_node
            return 

        # keep looping until you reach the end of the links 
        while current.next:
            current = current.next
        
        # set the last link's next link to the new node 
        current.next = new_node 

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if not self.head:
            return None 

        current = self.head 
        current_max_value = current.value 

        while current.next: 
            current_max_value = max(current.value, current_max_value)
            current = current.next
    
        # don't forget to check last one after loop ends  
        current_max_value = max(current.value, current_max_value)

        return current_max_value

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        if not self.head:
            return None 

        # if target value is first item in list, delete it  
        previous = self.head 
        if previous.value == value:
            self.head = previous.next # link previous to next
            return 

        # if target value is anywhere else, delete it 
        current = previous.next 
        while current:
            if current.value == value:
                previous.next = current.next # link previous to next   
                return 
            previous = current 
            current = current.next 


    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
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
        previous = None 
        current = self.head 

        while current:
            next = current.next # set a temp next to what is next 
            current.next = previous # set the next to what is currently previous 
            previous = current # set the previous to what is currently current 
            current = next # set what is current to temp variable 
        
        # set the final item to the final previous 
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

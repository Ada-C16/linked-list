
# Defines a node in the singly linked list
from distutils.command.build_scripts import first_line_re


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
        if self.head == None:
           return None
        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity:  O(1)
    # Space Complexity:  O(1)
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node   
        #=> DRY VERSION 
        # self.head = Node(value, self.head)

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity:  O(N)
    # Space Complexity:  O(N)
    def search(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def length(self):
        current = self.head  #initialize current 
        counter = 0
        
        while current:  #loop until current is None 
            counter += 1
            current = current.next
        return counter

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity:  O(N)
    # Space Complexity:  O(N)
    def get_at_index(self, index):
        if index < 0:
            return None
        current = self.head  
        counter = 0
        while current:
            if counter == index:
                return current.value
            counter +=1
            current = current.next #goes to next node
        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity:  O(N)
    # Space Complexity:  O(N)
    def get_last(self):
        if self.head == None:
            return None
        current = self.head 
        while current.next != None:
            current = current.next
        return current.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity:  O(N)
    # Space Complexity:  O(N)
    def add_last(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        current = self.head  
        if self.head == None:
            return None
        else:
            max_value = self.head.value
            while current:
                if current.value > max_value:
                    max_value = current.value
                current = current.next
            return max_value

    # method to delete the first node found with "specified value"
    # Time Complexity: O(N)
    # Space Complexity: O(N) like a search bcs specified value  
    def delete(self, value):
        if self.head == None:
            return None
        if self.head.value == value:
            self.head = self.head.next
            return
        previous = None
        current = self.head 
        while current != None:
            if current.value == value:
                previous.next = current.next      
            previous = current
            current = current.next
        return current

    # method to print all the values in the linked list
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def reverse(self):
        #initializes 
        previous = None
        current = self.head
        following = current.next
        
        while current:
            #reverse the pointers
            current.next = previous
            previous = current
            current = following
            #if there is a following node, set it to the current node
            if following:
                following = following.next
        # head is now the last node
        self.head = previous
  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity:  O(N)
    # Space Complexity:  O(N)
    def find_middle_value(self):
    # slow moves 1 step, fast moves 2, so when fast reaches the end the slow would be half way to the end
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer != None and fast_pointer.next != None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        return slow_pointer.value

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def find_nth_from_end(self, n):
         
        if self.head == None :
            return None 
        temp_index = self.length() - n -1    
        if temp_index < 0:
            return None  
        else:
            return self.get_at_index(temp_index)
        

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def has_cycle(self):
        current_node = self.head
        set_of_nodes_visited = set()
        while current_node != None:
            if current_node in set_of_nodes_visited:
                return True
            set_of_nodes_visited.add(current_node)
            current_node = current_node.next
        return False
    
    
        # slow_pointer = self.head
        # fast_pointer = self.head
        
        # while fast_pointer != None and fast_pointer.next != None:
        #     slow_pointer = slow_pointer.next
        #     fast_pointer = fast_pointer.next.next
        #     if slow_pointer == fast_pointer:
        #         return True
        # return False

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

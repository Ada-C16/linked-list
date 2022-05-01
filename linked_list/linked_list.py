#I am doing a doubly linked list instead
class Node:

    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next = next_node
        self.previous = prev_node

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
        #could be empty
        if not self.head:
            return None
        
        #if it is not empty, return the head node's value
        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_first(self, value):
        #could be empty
        if not self.head:
            #given that my list is empty,
            #i am making a new node
            #and this node is both the head the tail
            self.head = self.tail = Node(value)
        else:
            #i am still making a new node
            #and i want to assign the next value as the current head
            new_node = Node(value, self.head)
            #then i want to assign the node in front of the current head to the new node
            self.head.previous = new_node
            #and once that is done, I want to assign the new node as the new head
            self.head = new_node 
            #it has to be done in this order so that the chain isn't broken


    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        if not self.head:
            return False
        
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            else:
                current_node = current_node.next
        
        return False


    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        #if there's no head, the length is zero
        if not self.head:
            return 0
        #otherwise, how could I get the length?
        #by iterating
        #starting at the head, count until there's no self.next?
        counter = 0
        current_node = self.head
        while current_node: #while there is a next node,
            counter += 1 #add one to counter
            current_node = current_node.next #make the current node the next node
        
        return counter


    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        if not self.head:
            return None
        
        i = 0
        current_node = self.head
        while current_node: 
            if i == index:
                return current_node.value
            current_node = current_node.next 
            i += 1 

        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O()
    # Space Complexity: O(1)
    def get_last(self):
        #if my list is empty
        if not self.head:
            return None
        
        #if my list is one node 
        if self.head == self.tail:
            return self.head.value

        #if my list is longer than just one node
        return self.tail.value

        
    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_last(self, value):
        if not self.head:
            self.head = self.tail = Node(value)
        else:
            new_node = Node(value, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if not self.head:
            return None

        max = self.head.value
        current_node = self.head

        while current_node:
            if current_node.value > max:
                max = current_node.value
            else:
                current_node = current_node.next
        
        return max

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def delete(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                if current_node == self.head:
                    self.head = current_node.next
                    self.head.previous = None
                    return
                
                if current_node == self.tail:
                    self.tail = current_node.previous
                    self.tail.next = None
                    return

                current_node.previous.next = current_node.next
                current_node.next.previous = current_node.previous
                return
            else:
                current_node = current_node.next
        
    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1) .. or n?
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
        current_node = self.head
        while current_node:
            # next_node = current_node.next
            old_next = current_node.next
            old_previous = current_node.previous

            current_node.next = old_previous
            current_node.previous = old_next

            current_node = old_next

        old_head = self.head
        old_tail = self.tail

        self.head = old_tail
        self.tail = old_head
    
###############################################
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def find_middle_value(self):
        #use the functions I've already written
        #get the length
        #calculate middle index
        #pass that into get val at index
        length = self.length()
        middle = length // 2

        return self.get_at_index(middle)

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        length = self.length()
        target_index = length - n

        return self.get_at_index(target_index)

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

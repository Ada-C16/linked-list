
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
    # Time Complexity: ?
    # Space Complexity: ?
    def get_first(self):
        if self.head == None:
            return None
        else:
            return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def add_first(self, value):
        if self.head == None:
            new_node = Node(value=value, next_node=None)
            self.head= new_node
        else:
            new_node = Node(value=value, next_node=self.head)
            self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: ?
    # Space Complexity: ?
    def search(self, value):
        if self.head == None:
            return False
        else:
            current = self.head
            while current != None:
                if current.value == value:
                    return True
                else:
                    current = current.next
            return False
                

    # method that returns the length of the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def length(self):
        if self.head == None:
            return 0
        else:
            counter = 0
            current = self.head
            while current != None:
                counter += 1
                current = current.next
            return counter 

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: ?
    # Space Complexity: ?
    def get_at_index(self, index):
        if self.head == None:
            return None
        else:
            counter = 0 
            current = self.head
            while current != None:
                if counter == index:
                    return current.value
                else:
                    counter += 1
                    current = current.next
            return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: ?
    # Space Complexity: ?
    def get_last(self):
        if self.head == None:
            return None
        else:
            current = self.head
            while current != None:
                if current.next == None:
                    return current.value
                else:
                    current = current.next
            
                

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def add_last(self, value):
        new_node = Node(value, next_node=None)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current != None:
                if current.next == None:
                    new_node = Node(value, next_node=None)
                    current.next = new_node
                else:
                    current = current.next

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if self.head == None:
            return None
        else:
            final_max = self.head.value
            current = self.head.next
            while current != None:
                if current.value > final_max:
                    final_max = current.value
                current = current.next
            return final_max

                    

    # method to delete the first node found with specified value
    # Time Complexity: ?
    # Space Complexity: ?
    def delete(self, value):
        if self.head == None:
            return None
        elif self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next != None:
                if current.next.value == value:
                    current.next = current.next.next
                    return 
                else:
                    current = current.next

    # method to print all the values in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
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
        if self.head == None:
            return 
        elif self.head.next == None:
            return
        else:
            current = self.head
            reversed_link = None
            while current.next != None:
                if not reversed_link:
                    next_node = current.next
                    print(f"next_node: {next_node.value}")
                    current.next = None
                    reversed_link = current
                    print(f"reversed_link: {reversed_link.value}")
                    current = next_node
                    print(f"current: {current.value}")
                else:
                    print(f"**********")
                    print(f"hitting else block")
                    next_node = current.next
                    print(f"next_node: {next_node.value}")
                    current.next = reversed_link
                    reversed_link = current
                    current = next_node
                    print(f"current: {current.value}")
            current.next = reversed_link
            reversed_link = current
            self.head = reversed_link
            return self
        
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
    
    
    def print_list(self):
        current  = self.head
        while current != None:
            print(current.value)
            current = current.next
        return 
    
        
ll = LinkedList()
ll.add_first(3)
ll.add_first(2)
ll.add_first(1)
ll.add_first(0)

ll.reverse().print_list()

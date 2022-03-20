
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
    # Space Complexity: O(0)
    def get_first(self):
        if self.head is None:
            return None
        return self.head.value

    
    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def add_first(self, value):
        new_node = Node(value, self.head)
        if self.head == None:
            self.tail = new_node
        self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: ?
    # Space Complexity: ?
    def search(self, value):
        current = self.head
        if current is None:
            return False
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False


    # method that returns the length of the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def length(self):
        ctr = 0
        current = self.head
        while current is not None:
            ctr += 1
            current = current.next

        return ctr

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: ?
    # Space Complexity: ?
    def get_at_index(self, index):
        ctr = 0
        current = self.head
        while current is not None:
            if ctr == index:
                return current.value
            ctr += 1
            current = current.next
        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: ?
    # Space Complexity: ?
    def get_last(self):
        if self.head is None:
            return None

        # current = self.head
        # while current.next is not None:
        #     current = current.next
        # return current.value
        return self.tail.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
    def add_last(self, value):
        current = self.head
        if self.head is None:
            self.add_first(value)
            return
        while current.next is not None:
            current = current.next
        current.next = Node(value)
        self.tail = current.next
        

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        if self.head is None:
            return None
        high = self.head.value
        current = self.head
        while current is not None:
            if current.value > high:
                high = current.value
            current = current.next
        return high

    # method to delete the first node found with specified value
    # Time Complexity: ?
    # Space Complexity: ?
    def delete(self, value):

        current = self.head
        if current is None:
            return

        # head
        if current.value == value:
            self.head = current.next
            return 
        # middle
        while current.next is not None:
            if current.value == value:
                current.next = current.next.next
                return
                # if tail?
            prev = current
            current = current.next
        # tail
        if current.value == value:
            prev.next = None
            self.tail = prev

        # while node.val is not data:
        #         node = node.next
        #     node.val = node.next.val
        #     node.next = node.next.next

        # copy = self.head
        # # empty list
        
        # # first one is value
        # if copy.value == value:
        #     self.head = copy.next
        #     return 
        # # middle -> end
        # # while still in list
        #     # if current is match
        #         # stop
            
        # while copy is not None:
        #     if copy.value == value:
        #         prev.next = copy.next
        #         return
        #         # copy = None
        #     prev = copy
        #     copy = copy.next
        # if copy.value == value
        # current = self.head
        # if current is None:
        #     return 
        # # elif current == self.tail and current.value == value:
        # #     self.head = None
        # #     self.tail = None
        # #     return

        # if current.value == value:
        #     self.head = Node(self.head.next.value, self.head.next.next)
        #     return
        # while current.next is not None:
        #     if current.next.value == value:
        #             current.next = current.next.next
        #             self.tail = current
        #             return

        #     current = current.next
        # if self.head is None:
        #     return None
        # elif self.head == self.tail:
        #     self.head = None
        #     self.tail = None
        # else:
        #     current = self.head
        #     while current.next is not None:
        #         if current.value == value:
        #             if current.next == self.head:
        #                 self.head.value = self.head.next.value
        #                 self.head.next = self.head.next.next
                    
        #             if current.next.next is not None:
        #                 current.next = current.next.next
        #             else:
        #                 current.next = None
        #             return 
        #         current = current.next

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


    def delete_last(self):
        # empty
        if self.head is None:
            return
        # one element
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        # multiple
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        self.tail = current
        # current = self.head
        # while current.next.next is not None:
        #     prev = current
        #     current = current.next

        # prev = current.next
        # current.next = None
        # prev = None

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: ?
    # Space Complexity: ?
    def reverse(self):
        import copy
        # copy = self.head
        # tail = self.tail
        current = copy.deepcopy(self)
        self.head = None
        self.tail = None


        while current.head is not None: #:weary:
            self.add_last(current.get_last())
            current.delete_last()
 
        
        
        # copy = self.head
        # self.head = Node(self.get_last())
        # self.tail = self.head
        # # iterate through len(list) in reverse
        # for i in range(self.length()-1,0):
        #     self.head.next = Node(self.get_at_index(i))
        #     self.tail = self.head.next
        # # get index
        # # add last
  
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

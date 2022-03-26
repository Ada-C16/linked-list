from sqlalchemy import null


class Node:
    # Defines a node in the singly linked list
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node


class LinkedList:
    # Defines the singly linked list
    def __init__(self):
        self.head = None # keep the head private. Not accessible outside this class

    def get_first(self):
    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)    
        if self.head is None:
            return None
        
        return self.head.value

    def add_first(self, value):
    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: ?
    # Space Complexity: ?
        self.head = Node(value, self.head)


    def search(self, value):
    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: ?
    # Space Complexity: ?
        current = self.head

        while current:
            if current.value == value:
                return True
            else:
                current = current.next

        return False

    def length(self):
    # method that returns the length of the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?   
        current = self.head
        count = 0

        while current:
            current = current.next
            count += 1

        return count


    def get_at_index(self, index):
    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
        if index < 0:
            return None
        
        current_index = 0
        current = self.head

        while current and current_index < index:
            current = current.next
            current_index += 1

        if current is None:
            return None
        
        return current.value

    def get_last(self):
    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: ?
    # Space Complexity: ?
        current = self.head
        if current is None:
            return None
        
        while current:
            if current.next == None:
                break
            current = current.next

        return current.value

    def add_last(self, value):
    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: ?
    # Space Complexity: ?    
        current = self.head
        if current is None:
            self.head = Node(value, None)
        else:
            while current:
                if current.next == None:
                    break
                current = current.next

            current.next = Node(value, None)


    def find_max(self):
    # method to return the max value in the linked list
    # returns the data value and not the node    
        current = self.head
        if current is None:
            return None
        max = 0

        while current:
            if current.value > max:
                max = current.value
            current = current.next

        return max


    def delete(self, value):
    # method to delete the first node found with specified value
    # Time Complexity: ?
    # Space Complexity: ?    
        current = self.head
        prev = None
        if current is None:
            return None

        while current:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                    return
                prev.next = current.next
                return
            prev = current
            current = current.next



    def visit(self):
    # method to print all the values in the linked list
    # Time Complexity: ?
    # Space Complexity: ?
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))


    def reverse(self):
    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: ?
    # Space Complexity: ?    
        current = self.head
        prev = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


    def find_middle_value(self):
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?    
        current = self.head
        right = self.head
        
        while current:
            if current.next:
                current = current.next.next
                right = right.next
            else:
                current = current.next

        return right.value
        

    def find_nth_from_end(self, n):
    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?    
        len = self.length()
        index = len - n - 1

        return self.get_at_index(index)
        

    def has_cycle(self):
    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?    
        current = self.head
        nodes = set()

        while current: 
            if current in nodes:
                return True
            else:
                nodes.add(current)
            
            if current.next:
                current = current.next
            else:
                break
        return False
        

    def create_cycle(self):
    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node    
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node

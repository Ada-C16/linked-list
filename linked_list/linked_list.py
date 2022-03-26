
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
        if self.head is None:
            return None
        
        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        if self.head:
            current = self.head
            while current:
                if current.value == value:
                    return True
                else:
                    current = current.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        count = 0
        current = self.head

        while current:
            current = current.next
            count += 1

        return count

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        if index < 0:
            return 0
        
        current_index = 0
        current = self.head

        while current and current_index < index:
            current = current.next
            current_index += 1
        
        if current is None:
            return None
        
        return current.value

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if self.head is None:
            return None
        
        current = self.head

        while current.next:
            current = current.next
        
        return current.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        if self.head is None:
            self.add_first(value)
        else:
            current = self.head

            while current.next:
                current = current.next
            
            new_last = Node(value)
            current.next = new_last

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        current = self.head
        max_value = None

        while current:
            if max_value is None or current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        previous = None
        current = self.head

        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            else:
                previous = current
                current = current.next
        
        return None                

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
        previous = None
        current = self.head
        next_node = None

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous


    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        list_length = self.length()
        middle_index = list_length // 2
        return self.get_at_index(middle_index)



    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        list_length = self.length()
        index = list_length - n - 1
        if index < 0:
            return None
        return self.get_at_index(index)


    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(?)
    # Space Complexity: O(?)
    def has_cycle(self):
        current = self.head
        visited = set()

        while current:
            if current in visited:
                return True
            else:
                visited.add(current)
                current = current.next

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

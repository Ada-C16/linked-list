
# Defines a node in the singly linked list
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
        if self.head is None:
            return None
        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            new_node = Node(value, self.head)
            self.head.previous = new_node
            self.head = new_node

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

        

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        list_loc = 0
        current = self.head
        while current is not None:
            if list_loc == index:
                return current.value
            list_loc += 1
            current = current.next
        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_last(self):
        if self.head is None:
            return None
        return self.tail.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_last(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else: 
            new_node = Node(value, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node

    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_max(self):
        max = None
        current = self.head
        while current is not None:
            if max is None:
                max = current.value
            elif current.value > max:
                max = current.value
            current = current.next
        return max

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def delete(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                next_node = current.next
                prev_node = current.previous
                # When current is Head
                if current == self.head:
                    next_node.previous = None
                    self.head = next_node
                    return
                # When current is Tail
                elif current == self.tail:
                    prev_node.next = None
                    self.tail = prev_node
                    return
                # When current is in the middle
                else:
                    prev_node.next = current.next
                    next_node.previous = current.previous
                    return
            else:
                current = current.next
                


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
        if self.head == self.tail:
            return
        
        current = self.head
        while current is not None:
            prev = current.previous
            next = current.next
            current.next = prev
            current.previous = next
            current = next
        
        temp = self.head
        self.head = self.tail
        self.tail = temp


    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        index_loc = self.length() // 2
        return self.get_at_index(index_loc)
    


    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        last_index = self.length() - 1
        if last_index - n >= 0:
            return self.get_at_index(last_index - n)
        return

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def has_cycle(self):
        visited_nodes = set()
        current = self.head
        while current is not None:
            if current in visited_nodes:
                return True
            else: 
                visited_nodes.add(current)
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
